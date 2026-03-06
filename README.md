Basic usages (only specify the count of dimensions):

```python
import torch
from statictorch import *

def f(x: Tensor2d):
    pass

f(torch.zeros([2, 3]))  # No runtime error, but static type checkers might say: "Tensor" is not assignable to "Tensor2d"
f(Tensor2d(torch.zeros([2, 3])))  # It's ok.
```

Note that `TensorXd()` directly return the given tensor. So at runtime you can't distinguish `x` and `TensorXd(x)`, and `isinstance(TensorXd(x), TensorXd)` will return `False`.

`TensorXd` is defined as generic classes, so that you could add a dimension descriptor for them:

```python
from statictorch import *

# In previous versions, inheriting from TensorDimensionDescriptor was mandatory. 
# While this requirement is now relaxed to accommodate the new TypeVarTuple-based TensorNd, 
# it remains highly recommended for better semantic clarity and consistency.
class Batch(TensorDimensionDescriptor):
    pass

class Channel(TensorDimensionDescriptor):
    pass

class Sample(TensorDimensionDescriptor):
    pass

def train_on(x: Tensor3d[Batch, Channel, Sample], y: Tensor3d[Channel, Batch, Sample]):
    ...

def load_data() -> tuple[Tensor3d[Batch, Channel, Sample], Tensor3d[Batch, Channel, Sample]]:
    ...

data_x, data_y = load_data()
train_on(data_x, data_y)  # Pylance: Argument of type "Tensor3d[Batch, Channel, Sample]" cannot be assigned to parameter "y" of type "Tensor3d[Channel, Batch, Sample]" in function "train_on"

# To solve the problem:
data_y_transposed = data_y.transpose(1, 0)
train_on(data_x, Tensor3d(data_y_transposed))

# Of course in some cases you want to force passing data_y, just simply cheating the type checker with:
train_on(data_x, Tensor3d(data_y))
```

`typing.cast` is also a good idea, especially when you want to call functions like `torch.stack` on a `list[TensorXd]`:

```python
import statictorch
import typing
from torch import Tensor

def work_on(tensors: list[Tensor]):
    ...

my_tensors: list[statictorch.Tensor0d] = []
work_on(my_tensors)  # Pylance: Argument of type "list[Tensor0d]" cannot be assigned to parameter "tensors" of type "list[Tensor]" in function "work_on"

# To solve the problem:
work_on(typing.cast(list[Tensor], my_tensors))

# If you find typing.cast too long:
work_on(statictorch.anify(my_tensors))

# If the function is defined by yourself, use Sequence when applicable:
def my_work_on(tensors: typing.Sequence[Tensor]):
    ...
my_work_on(my_tensors)  # Ok, as Sequence is covariant.
```

In the new version, we introduce `TensorNd`, which supports an arbitrary number of dimensions:

```python
from typing import Any
import torch
from statictorch.tensor_nd import Tensor3d, TensorNd


# a 15-d tensor
t15: TensorNd[Any, Any, Any, Any, Any,
              Any, Any, Any, Any, Any, 
              Any, Any, Any, Any, Any] = TensorNd(torch.zeros([1] * 15))


t2: TensorNd[Any, Any] = TensorNd(torch.zeros([1, 1]))
t3: TensorNd[Any, Any, Any] = t2  # Pylance: Type "TensorNd[Any, Any]" is not assignable to declared type "TensorNd[Any, Any, Any]"


# Due to technical limitations in Python, we must define TensorXd using inheritance.
# As a result, a TensorNd cannot be directly assigned to a TensorXd even if their dimensions match.
t3_: Tensor3d = t3  # Pylance: Type "TensorNd[Any, Any, Any]" is not assignable to declared type "Tensor3d[Unknown, Unknown, Unknown]"
# Conversely, a Tensor3d can be used directly as a TensorNd.
t3 = t3_
```