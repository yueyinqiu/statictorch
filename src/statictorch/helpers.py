from typing import Any, TypeAlias

from torch import Tensor

TensorAny: TypeAlias = Tensor
"""DEPRECATED: Use TensorNd instead. This alias will be removed in future versions."""

def anify(object: Any) -> Any:
    return object