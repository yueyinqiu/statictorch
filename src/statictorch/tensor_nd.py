from typing import Generic, Self, TypeVarTuple
import typing
from torch import Tensor


_T = TypeVarTuple("_T")
class TensorNd(Tensor, Generic[*_T]):
    def __new__(cls, tensor: Tensor) -> Self:
        return typing.cast(Self, tensor)

    def __init__(self, tensor: Tensor):
        raise RuntimeError("TensorNd.__init__ only exists for type annotation and should never be called in runtime.")


class Tensor0d(TensorNd[*tuple[()]]): pass
class Tensor1d[T1](TensorNd[T1]): pass
class Tensor2d[T1, T2](TensorNd[T1, T2]): pass
class Tensor3d[T1, T2, T3](TensorNd[T1, T2, T3]): pass
class Tensor4d[T1, T2, T3, T4](TensorNd[T1, T2, T3, T4]): pass
class Tensor5d[T1, T2, T3, T4, T5](TensorNd[T1, T2, T3, T4, T5]): pass
class Tensor6d[T1, T2, T3, T4, T5, T6](TensorNd[T1, T2, T3, T4, T5, T6]): pass
class Tensor7d[T1, T2, T3, T4, T5, T6, T7](TensorNd[T1, T2, T3, T4, T5, T6, T7]): pass
class Tensor8d[T1, T2, T3, T4, T5, T6, T7, T8](TensorNd[T1, T2, T3, T4, T5, T6, T7, T8]): pass
class Tensor9d[T1, T2, T3, T4, T5, T6, T7, T8, T9](TensorNd[T1, T2, T3, T4, T5, T6, T7, T8, T9]): pass
