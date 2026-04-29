from typing import Any
import typing

import torch

from statictorch.tensor_nd import TensorNd

def anify(object: Any) -> Any:
    return object

def cat[T: TensorNd](
    tensors: tuple[T, ...] | list[T] | None,
    dim: int = 0,
    *,
    out: torch.Tensor | None = None,
) -> torch.Tensor:
    return torch.cat(typing.cast(tuple[torch.Tensor, ...] | list[torch.Tensor], tensors), 
                     dim, 
                     out=out)

def stack[T: TensorNd](
    tensors: tuple[T, ...] | list[T] | None,
    dim: int = 0,
    *,
    out: torch.Tensor | None = None,
) -> torch.Tensor:
    return torch.stack(typing.cast(tuple[torch.Tensor, ...] | list[torch.Tensor], tensors), 
                       dim, 
                       out=out)
