try:
    import torch
    
    e: ImportError
except ImportError as e:
    raise ImportError(
        "Missing dependency: 'torch'. "
        "Although it is not listed as a hard dependency (to avoid version conflicts), 'likb' requires PyTorch. "
        "Please install a appropriate version of PyTorch."
    ) from e

from statictorch.tensor_nd import (
    TensorNd as TensorNd,
    Tensor0d as Tensor0d,
    Tensor1d as Tensor1d,
    Tensor2d as Tensor2d,
    Tensor3d as Tensor3d,
    Tensor4d as Tensor4d,
    Tensor5d as Tensor5d,
    Tensor6d as Tensor6d,
    Tensor7d as Tensor7d,
    Tensor8d as Tensor8d,
    Tensor9d as Tensor9d,
)

from statictorch.tensor_dimension_descriptor import TensorDimensionDescriptor as TensorDimensionDescriptor

from statictorch.helpers import anify as anify
from statictorch.helpers import TensorAny as TensorAny
