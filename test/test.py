from statictorch import *

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
train_on(data_x, data_y)
# If you are using Pylance it will say:
# Argument of type "Tensor3d[Batch, Channel, Sample]" cannot be assigned to parameter "y" of type "Tensor3d[Channel, Batch, Sample]" in function "train_on"

# To solve the problem:
data_y_transposed = data_y.transpose(1, 0)
train_on(data_x, Tensor3d(data_y_transposed))

# Of course in some cases you want to force passing data_y, just simply cheating the type checker with:
train_on(data_x, Tensor3d(data_y))
