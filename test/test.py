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
t3_: Tensor3d = t3  # Type "TensorNd[Any, Any, Any]" is not assignable to declared type "Tensor3d[Unknown, Unknown, Unknown]"
# Conversely, a Tensor3d can be used directly as a TensorNd.
t3 = t3_
