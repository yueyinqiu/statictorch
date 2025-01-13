print(
"""# Generated with statictorch/generator/generator.py
import typing as _typing
import torch as _torch


class TensorDimensionDescriptor:
    def __init__(self):
        raise RuntimeError('TensorDimensionDescriptor only exists for type annotation and should not be initialized.')

"""
)

i = 0
print(f"class Tensor{i}d(_torch.Tensor):")
print(f"    def __new__(cls, tensor: _torch.Tensor) -> 'Tensor{i}d':")
print(f"        return tensor  # type: ignore")
print()
print(f"    def __init__(self, tensor: _torch.Tensor):")
print(f"        super().__init__()")
print(f"        raise RuntimeError('Tensor{i}d.__init__ only exists for type annotation and should not be called in runtime.')")

for i in range(1, 10):
    print()
    print()
    print(f"_T{i} = _typing.TypeVar('_T{i}', bound=TensorDimensionDescriptor)")
    generic_parameters = ", ".join(f"_T{j}" for j in range(1, i + 1))
    print(f"class Tensor{i}d(_torch.Tensor, _typing.Generic[{generic_parameters}]):")
    print(f"    def __new__(cls, tensor: _torch.Tensor) -> 'Tensor{i}d':")
    print(f"        return tensor  # type: ignore")
    print()
    print(f"    def __init__(self, tensor: _torch.Tensor):")
    print(f"        super().__init__()")
    print(f"        raise RuntimeError('Tensor{i}d.__init__ only exists for type annotation and should not be called in runtime.')")