"""Stubs for more_itertools.recipes"""
from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
)
from typing_extensions import overload, Type

# Type and type variable definitions
_T = TypeVar('_T')
_U = TypeVar('_U')

def take(n: int, iterable: Iterable[_T]) -> List[_T]: ...
def tabulate(
    function: Callable[[int], _T], start: int = ...
) -> Iterator[_T]: ...
def tail(n: int, iterable: Iterable[_T]) -> Iterator[_T]: ...
def consume(iterator: Iterable[object], n: Optional[int] = ...) -> None: ...
@overload
def nth(iterable: Iterable[_T], n: int) -> Optional[_T]: ...
@overload
def nth(iterable: Iterable[_T], n: int, default: _U) -> Union[_T, _U]: ...
def all_equal(iterable: Iterable[object]) -> bool: ...
def quantify(
    iterable: Iterable[_T], pred: Callable[[_T], bool] = ...
) -> int: ...
def pad_none(iterable: Iterable[_T]) -> Iterator[Optional[_T]]: ...
def padnone(iterable: Iterable[_T]) -> Iterator[Optional[_T]]: ...
def ncycles(iterable: Iterable[_T], n: int) -> Iterator[_T]: ...
def dotproduct(vec1: Iterable[object], vec2: Iterable[object]) -> object: ...
def flatten(listOfLists: Iterable[Iterable[_T]]) -> Iterator[_T]: ...
def repeatfunc(
    func: Callable[..., _U], times: Optional[int] = ..., *args: Any
) -> Iterator[_U]: ...
def pairwise(iterable: Iterable[_T]) -> Iterator[Tuple[_T, _T]]: ...
@overload
def grouper(
    iterable: Iterable[_T],
    n: int,
    incomplete: str = ...,
    fillvalue: _U = ...,
) -> Iterator[Tuple[Union[_T, _U], ...]]: ...
@overload
def grouper(  # Deprecated interface
    iterable: int,
    n: Iterable[_T],
    incomplete: str = ...,
    fillvalue: _U = ...,
) -> Iterator[Tuple[Union[_T, _U], ...]]: ...
def roundrobin(*iterables: Iterable[_T]) -> Iterator[_T]: ...
def partition(
    pred: Optional[Callable[[_T], object]], iterable: Iterable[_T]
) -> Tuple[Iterator[_T], Iterator[_T]]: ...
def powerset(iterable: Iterable[_T]) -> Iterator[Tuple[_T, ...]]: ...
def unique_everseen(
    iterable: Iterable[_T], key: Optional[Callable[[_T], _U]] = ...
) -> Iterator[_T]: ...
def unique_justseen(
    iterable: Iterable[_T], key: Optional[Callable[[_T], object]] = ...
) -> Iterator[_T]: ...
@overload
def iter_except(
    func: Callable[[], _T],
    exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
    first: None = ...,
) -> Iterator[_T]: ...
@overload
def iter_except(
    func: Callable[[], _T],
    exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
    first: Callable[[], _U],
) -> Iterator[Union[_T, _U]]: ...
@overload
def first_true(
    iterable: Iterable[_T], *, pred: Optional[Callable[[_T], object]] = ...
) -> Optional[_T]: ...
@overload
def first_true(
    iterable: Iterable[_T],
    default: _U,
    pred: Optional[Callable[[_T], object]] = ...,
) -> Union[_T, _U]: ...
def random_product(
    *args: Iterable[_T], repeat: int = ...
) -> Tuple[_T, ...]: ...
def random_permutation(
    iterable: Iterable[_T], r: Optional[int] = ...
) -> Tuple[_T, ...]: ...
def random_combination(iterable: Iterable[_T], r: int) -> Tuple[_T, ...]: ...
def random_combination_with_replacement(
    iterable: Iterable[_T], r: int
) -> Tuple[_T, ...]: ...
def nth_combination(
    iterable: Iterable[_T], r: int, index: int
) -> Tuple[_T, ...]: ...
def prepend(value: _T, iterator: Iterable[_U]) -> Iterator[Union[_T, _U]]: ...
def convolve(signal: Iterable[_T], kernel: Iterable[_T]) -> Iterator[_T]: ...
def before_and_after(
    predicate: Callable[[_T], bool], it: Iterable[_T]
) -> Tuple[Iterator[_T], Iterator[_T]]: ...
def triplewise(iterable: Iterable[_T]) -> Iterator[Tuple[_T, _T, _T]]: ...
def sliding_window(
    iterable: Iterable[_T], n: int
) -> Iterator[Tuple[_T, ...]]: ...
def subslices(iterable: Iterable[_T]) -> Iterator[List[_T]]: ...
def polynomial_from_roots(roots: Sequence[int]) -> List[int]: ...
def sieve(n: int) -> Iterator[int]: ...
