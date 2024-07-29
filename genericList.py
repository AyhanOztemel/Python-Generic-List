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
    
    def _check_type(self, item: T) -> None:
        if not isinstance(item, self._allowed_types):
            raise TypeError(f"Sadece {self._allowed_types} türleri eklenebilir")

    def extend(self, items: List[T]) -> None:
        for item in items:
            self._check_type(item)
        self._list.extend(items)

    def insert(self, index: int, item: T) -> None:
        self._check_type(item)
        self._list.insert(index, item)

    def remove(self, item: T) -> None:
        self._check_type(item)
        self._list.remove(item)

    def pop(self, index: int = -1) -> T:
        return self._list.pop(index)

    def clear(self) -> None:
        self._list.clear()

    def index(self, item: T, start: int = 0, end: int = -1) -> int:
        self._check_type(item)
        return self._list.index(item, start, end if end != -1 else len(self._list))

    def count(self, item: T) -> int:
        self._check_type(item)
        return self._list.count(item)

    def sort(self, *, key=None, reverse: bool = False) -> None:
        self._list.sort(key=key, reverse=reverse)

    def reverse(self) -> None:
        self._list.reverse()

    def copy(self) -> 'TypedList':
        new_list = TypedList(self._allowed_types)
        new_list._list = self._list.copy()
        return new_list
    def __contains__(self, item: T) -> bool:
        self._check_type(item)
        return item in self._list

    def __delitem__(self, index: int) -> None:
        del self._list[index]

    def __reversed__(self):
        return reversed(self._list)
   

    def __repr__(self) -> str:
        return repr(self._list)




