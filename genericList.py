from typing import TypeVar, Generic, List, Union, Type

T = TypeVar('T')

class TypeSafeList(Generic[T]):
    def __init__(self, allowed_types: Union[Type, tuple]):
        self._allowed_types = allowed_types if isinstance(allowed_types, tuple) else (allowed_types,)
        self._list: List[T] = []

    def append(self, item: T) -> None:
        if not isinstance(item, self._allowed_types):
            raise TypeError(f"Only {self._allowed_types} types can be added")
        self._list.append(item)

    def __getitem__(self, index: int) -> T:
        return self._list[index]
    
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self._allowed_types):
            raise TypeError(f"Sadece {self._allowed_types} türleri atanabilir")
        self._list[index] = item

    def __len__(self) -> int:
        return len(self._list)

    def __iter__(self):
        return iter(self._list)

    def __str__(self):
        return str(self._list)


