from collections.abc import Iterator
from typing import Any, Literal, SupportsIndex, overload
from typing_extensions import Self, TypeIs

import numpy as np
import numpy.typing as npt

from ._base import sparray
from ._bsr import bsr_array, bsr_matrix
from ._coo import coo_array, coo_matrix
from ._csc import csc_array, csc_matrix
from ._dia import dia_array, dia_matrix
from ._dok import dok_array, dok_matrix
from ._index import IndexMixin
from ._lil import lil_array, lil_matrix
from ._matrix import spmatrix
from .typing import (
    _SCT,
    SparseArray,
    _ArrayLike1DDual,
    _ArrayLike1DIndex,
    _ArrayType,
    _BoolLike_co,
    _CastingKind,
    _DType_co,
    _DTypeLike,
    _Formats,
    _NumberLike_co,
    _OrderType,
    _SCT_co,
    _SCT_uifcO,
    _ShapeAnno,
    _ShapeLike,
)

__all__ = ["csr_array", "csr_matrix", "isspmatrix_csr"]

def isspmatrix_csr(x: Any) -> TypeIs[csr_matrix[Any, Any]]: ...

class csr_array(sparray[_ShapeAnno, _DType_co], IndexMixin):
    ###########################################################################
    # common attributes / methods common to all sparray/spmatrix
    # inherited from private base class _spbase
    ###########################################################################

    __array_priority__: float
    @property
    def ndim(self) -> int: ...
    maxprint: int
    @property
    def shape(self) -> tuple[int, ...]: ...
    def __iter__(self) -> Iterator[Any]: ...
    def count_nonzero(self) -> int: ...
    @property
    def nnz(self) -> int: ...
    @property
    def size(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> Any: ...
    def __ne__(self, other: object) -> Any: ...
    def __lt__(self, other: object) -> Any: ...
    def __gt__(self, other: object) -> Any: ...
    def __le__(self, other: object) -> Any: ...
    def __ge__(self, other: object) -> Any: ...
    def conjugate(self, copy: bool = ...) -> Self: ...
    def conj(self, copy: bool = ...) -> Self: ...
    def nonzero(
        self,
    ) -> tuple[
        np.ndarray[Any, np.dtype[np.int_]], np.ndarray[Any, np.dtype[np.int_]]
    ]: ...
    @overload
    def toarray(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def toarray(self, order: None, out: _ArrayType) -> _ArrayType: ...
    @overload
    def toarray(self, order: None = ..., *, out: _ArrayType) -> _ArrayType: ...
    def copy(self) -> Self: ...
    def diagonal(self, k: SupportsIndex = ...) -> np.ndarray[Any, _DType_co]: ...
    def setdiag(self, values: npt.ArrayLike, k: SupportsIndex = ...) -> None: ...
    @overload
    def resize(self, shape: _ShapeLike) -> None: ...
    @overload
    def resize(self, *shape: SupportsIndex) -> None: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.bool_ | np.int_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.int_: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def sum(
        self: csr_array[Any, Any],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.bool_ | np.int_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.int_]]: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.unsignedinteger[Any]]]: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.float_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.float_]]: ...
    @overload
    def sum(
        self: csr_array[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.complex_]]: ...
    @overload
    def sum(
        self: csr_array[Any, Any],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, Any]: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        *,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: None,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[_SCT]]: ...
    @overload
    def sum(
        self,
        axis: None,
        dtype: npt.DTypeLike,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        *,
        dtype: npt.DTypeLike = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: npt.DTypeLike,
        out: None = ...,
    ) -> np.ndarray[Any, Any]: ...
    @overload
    def sum(
        self,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex | None = ...,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        *,
        out: _ArrayType,
        dtype: npt.DTypeLike | None = ...,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex | None,
        dtype: npt.DTypeLike | None,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def trace(
        self: csr_array[Any, np.dtype[np.bool_ | np.int_]],
        offset: SupportsIndex = ...,
    ) -> np.int_: ...
    @overload
    def trace(
        self: csr_array[Any, np.dtype[np.unsignedinteger[Any]]],
        offset: SupportsIndex = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def trace(
        self: csr_array[Any, np.dtype[np.float_]],
        offset: SupportsIndex = ...,
    ) -> np.float_: ...
    @overload
    def trace(
        self: csr_array[Any, np.dtype[np.complex_]],
        offset: SupportsIndex = ...,
    ) -> np.complex_: ...
    @overload
    def trace(self: csr_array[Any, Any], offset: SupportsIndex = ...) -> Any: ...
    @overload
    def todense(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def todense(self, *, out: _ArrayType) -> _ArrayType: ...
    @overload
    def todense(self, order: None, out: _ArrayType) -> _ArrayType: ...
    def tocsr(self, copy: bool = ...) -> csr_array[_ShapeAnno, _DType_co]: ...
    def todok(self, copy: bool = ...) -> dok_array[_ShapeAnno, _DType_co]: ...
    def tocoo(self, copy: bool = ...) -> coo_array[_ShapeAnno, _DType_co]: ...
    def tolil(self, copy: bool = ...) -> lil_array[_ShapeAnno, _DType_co]: ...
    def todia(self, copy: bool = ...) -> dia_array[_ShapeAnno, _DType_co]: ...
    def tobsr(
        self,
        blocksize: tuple[SupportsIndex, SupportsIndex] | None = ...,
        copy: bool = ...,
    ) -> bsr_array[_ShapeAnno, _DType_co]: ...
    def tocsc(self, copy: bool = ...) -> csc_array[_ShapeAnno, _DType_co]: ...
    @overload
    def mean(
        self: sparray[Any, np.dtype[np.bool_ | np.integer[Any] | np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def mean(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def mean(
        self: sparray[Any, Any], axis: None = ..., dtype: None = ..., out: None = ...
    ) -> Any: ...
    @overload
    def mean(
        self, axis: None = ..., *, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> _SCT: ...
    @overload
    def mean(self, axis: None, dtype: _DTypeLike[_SCT], out: None = ...) -> _SCT: ...
    @overload
    def mean(
        self, axis: None = ..., *, dtype: npt.DTypeLike, out: None = ...
    ) -> Any: ...
    @overload
    def mean(self, axis: None, dtype: npt.DTypeLike, out: None = ...) -> Any: ...
    @overload
    def mean(
        self: (
            sparray[Any, np.dtype[np.bool_]]
            | sparray[Any, np.dtype[np.integer[Any]]]
            | sparray[Any, np.dtype[np.float_]]
        ),
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.float_]] | np.float_: ...
    @overload
    def mean(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.complex_]] | np.complex_: ...
    @overload
    def mean(
        self, axis: SupportsIndex, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> np.ndarray[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex,
        dtype: npt.DTypeLike | None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def mean(
        self,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex | None = ...,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        *,
        dtype: npt.DTypeLike | None = ...,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex | None,
        dtype: npt.DTypeLike | None,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def asformat(self, format: None, copy: bool = ...) -> Self: ...
    @overload
    def asformat(
        self, format: Literal["csr"], copy: bool = ...
    ) -> csr_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dok"], copy: bool = ...
    ) -> dok_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["coo"], copy: bool = ...
    ) -> coo_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["lil"], copy: bool = ...
    ) -> lil_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dia"], copy: bool = ...
    ) -> dia_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["bsr"], copy: bool = ...
    ) -> bsr_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["csc"], copy: bool = ...
    ) -> csc_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["array", "dense"]
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self,
        format: _Formats | None,
        copy: bool = ...,
    ) -> sparray[_ShapeAnno, _DType_co]: ...
    # In reshape, copy=False annotating is problematic, but I decided to copy from
    # numpy where it is permitted to mutate the shape without changing the ShapeType
    # typevar.
    @overload
    def reshape(
        self,
        shape: _ShapeLike,
        /,
        *,
        order: _OrderType | None = ...,
        copy: bool = ...,
    ) -> sparray[Any, _DType_co]: ...
    @overload
    def reshape(
        self,
        *shape: SupportsIndex,
        order: _OrderType | None = ...,
        copy: bool = ...,
    ) -> sparray[Any, _DType_co]: ...
    @overload
    def astype(
        self,
        dtype: _DTypeLike[_SCT],
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> csr_array[Any, np.dtype[_SCT]]: ...
    @overload
    def astype(
        self,
        dtype: npt.DTypeLike,
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> csr_array[Any, Any]: ...
    @property
    def real(self) -> csr_array[_ShapeAnno, Any]: ...
    @property
    def imag(self) -> csr_array[_ShapeAnno, Any]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: None = ...,
    ) -> csr_array[_ShapeAnno, Any]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: _DTypeLike[_SCT],
    ) -> csr_array[_ShapeAnno, np.dtype[_SCT]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: npt.DTypeLike,
    ) -> csr_array[_ShapeAnno, Any]: ...
    def __abs__(self) -> csr_array[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: csr_array[Any, np.dtype[np.bool_]],
        ndigits: SupportsIndex = ...,
    ) -> csr_array[_ShapeAnno, np.dtype[np.float16]]: ...
    @overload
    def __round__(
        self: csr_array[Any, np.dtype[np.complex_ | np.object_]],
        ndigits: SupportsIndex = ...,
    ) -> csr_array[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: csr_array[Any, np.dtype[_SCT_uifcO]],
        ndigits: SupportsIndex = ...,
    ) -> csr_array[_ShapeAnno, np.dtype[_SCT_uifcO]]: ...
    @overload
    def __round__(
        self: csr_array[Any, Any],
        ndigits: SupportsIndex = ...,
    ) -> csr_array[_ShapeAnno, Any]: ...
    # TODO: The return type of __add__ can be refined
    def __add__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __radd__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __sub__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rsub__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __matmul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rmatmul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __truediv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __div__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rtruediv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rdiv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __iadd__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __isub__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __imul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __idiv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __itruediv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    # TODO: the type annotations of multiply, maximum, minimum and dot can be refined
    def multiply(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def maximum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def minimum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def dot(
        self, other: npt.ArrayLike | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    @property
    def T(self) -> csc_array[Any, _DType_co] | csr_array[Any, _DType_co]: ...
    def transpose(
        self, axes: None = ..., copy: bool = ...
    ) -> csc_array[Any, _DType_co] | csr_array[Any, _DType_co]: ...
    ###########################################################################
    # common methods/attributes from _cs_matrix
    ###########################################################################
    data: np.ndarray[Any, _DType_co]
    indices: np.ndarray[Any, np.dtype[np.int_]]
    indptr: np.ndarray[Any, np.dtype[np.int_]]
    def check_format(self, full_check: bool = ...) -> None: ...
    def eliminate_zeros(self) -> None: ...
    @property
    def has_canonical_format(self) -> bool: ...
    @has_canonical_format.setter
    def has_canonical_format(self, val: bool) -> None: ...
    def sum_duplicates(self) -> None: ...
    @property
    def has_sorted_indices(self) -> bool: ...
    @has_sorted_indices.setter
    def has_sorted_indices(self, val: _BoolLike_co) -> None: ...
    def sorted_indices(self) -> Self: ...
    def sort_indices(self) -> None: ...
    def prune(self) -> None: ...
    # input is sparse array/matrix
    @overload
    def __init__(
        self,
        arg1: sparray[Any, _DType_co] | spmatrix[Any, _DType_co],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: SparseArray[Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: SparseArray[Any],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: SparseArray[Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: SparseArray[Any],
        shape: _ShapeLike | None,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    # input is shape and dtype to init empty sparse
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[SupportsIndex] | tuple[SupportsIndex, SupportsIndex],
        *,
        dtype: _DTypeLike[_SCT_co],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: tuple[SupportsIndex] | tuple[SupportsIndex, SupportsIndex],
        *,
        dtype: npt.DTypeLike | None = ...,
    ) -> None: ...
    # input is data and indices
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            np.ndarray[Any, np.dtype[_SCT_co]],
            tuple[_ArrayLike1DIndex],
        ]
        | tuple[
            np.ndarray[Any, np.dtype[_SCT_co]],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex],
        ]
        | tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex],
        ]
        | tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex],
        ]
        | tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None = ...,
        dtype: npt.DTypeLike | None = ...,
        copy: bool = ...,
    ) -> None: ...
    # input is data, indices, indptr
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            np.ndarray[Any, np.dtype[_SCT_co]],
            _ArrayLike1DIndex,
            _ArrayLike1DIndex,
        ],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        dtype: npt.DTypeLike | None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: np.ndarray[Any, np.dtype[_SCT_co]],
        *,
        dtype: None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_array[Any, np.dtype[_SCT_co]],
        arg1: npt.ArrayLike,
        *,
        dtype: _DTypeLike[_SCT_co],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: npt.ArrayLike,
        *,
        dtype: npt.DTypeLike | None = ...,
    ) -> None: ...
    ###########################################################################
    # common methods from _data_matrix
    ###########################################################################
    @property
    def dtype(self) -> _DType_co: ...
    # as for ndarray, the dtype.setter is not type annotated
    def _deduped_data(self) -> np.ndarray[Any, _DType_co]: ...

    # dynamically set unary ufuncs:
    def sin(self) -> csr_array[_ShapeAnno, Any]: ...
    def tan(self) -> csr_array[_ShapeAnno, Any]: ...
    def arcsin(self) -> csr_array[_ShapeAnno, Any]: ...
    def arctan(self) -> csr_array[_ShapeAnno, Any]: ...
    def sinh(self) -> csr_array[_ShapeAnno, Any]: ...
    def tanh(self) -> csr_array[_ShapeAnno, Any]: ...
    def arcsinh(self) -> csr_array[_ShapeAnno, Any]: ...
    def arctanh(self) -> csr_array[_ShapeAnno, Any]: ...
    def rint(self) -> csr_array[_ShapeAnno, Any]: ...
    def sign(self) -> csr_array[_ShapeAnno, Any]: ...
    def expm1(self) -> csr_array[_ShapeAnno, Any]: ...
    def log1p(self) -> csr_array[_ShapeAnno, Any]: ...
    def deg2rad(self) -> csr_array[_ShapeAnno, Any]: ...
    def rad2deg(self) -> csr_array[_ShapeAnno, Any]: ...
    def floor(self) -> csr_array[_ShapeAnno, Any]: ...
    def ceil(self) -> csr_array[_ShapeAnno, Any]: ...
    def trunc(self) -> csr_array[_ShapeAnno, Any]: ...
    def sqrt(self) -> csr_array[_ShapeAnno, Any]: ...
    ###########################################################################
    # common methods from _minmax_mixin
    ###########################################################################
    @overload
    def max(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def max(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def max(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_array[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def max(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_array | np.number[Any]: ...
    @overload
    def min(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def min(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def min(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_array[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def min(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_array | np.number[Any]: ...
    @overload
    def nanmax(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def nanmax(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmax(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_array[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def nanmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_array | np.number[Any]: ...
    @overload
    def nanmin(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def nanmin(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmin(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_array[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def nanmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_array | np.number[Any]: ...
    @overload
    def argmax(self, axis: None = ..., out: None = ...) -> np.int_: ...
    @overload
    def argmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> np.ndarray[Any, np.dtype[np.int_]] | np.int_: ...
    @overload
    def argmin(self, axis: None = ..., out: None = ...) -> np.int_: ...
    @overload
    def argmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> np.ndarray[Any, np.dtype[np.int_]] | np.int_: ...
    @property
    def format(self) -> Literal["csr"]: ...

class csr_matrix(spmatrix[_ShapeAnno, _DType_co], IndexMixin):
    ###########################################################################
    # common attributes / methods common to all sparray/spmatrix
    # inherited from private base class _spbase
    ###########################################################################

    __array_priority__: float
    @property
    def ndim(self) -> int: ...
    maxprint: int
    @property
    def shape(self) -> tuple[int, ...]: ...
    def __iter__(self) -> Iterator[Any]: ...
    def count_nonzero(self) -> int: ...
    @property
    def nnz(self) -> int: ...
    @property
    def size(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __nonzero__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> Any: ...
    def __ne__(self, other: object) -> Any: ...
    def __lt__(self, other: object) -> Any: ...
    def __gt__(self, other: object) -> Any: ...
    def __le__(self, other: object) -> Any: ...
    def __ge__(self, other: object) -> Any: ...
    def conjugate(self, copy: bool = ...) -> Self: ...
    def conj(self, copy: bool = ...) -> Self: ...
    def nonzero(
        self,
    ) -> tuple[
        np.ndarray[Any, np.dtype[np.int_]], np.ndarray[Any, np.dtype[np.int_]]
    ]: ...
    @overload
    def toarray(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def toarray(self, order: None, out: _ArrayType) -> _ArrayType: ...
    @overload
    def toarray(self, order: None = ..., *, out: _ArrayType) -> _ArrayType: ...
    def copy(self) -> Self: ...
    def diagonal(self, k: SupportsIndex = ...) -> np.ndarray[Any, _DType_co]: ...
    def setdiag(self, values: npt.ArrayLike, k: SupportsIndex = ...) -> None: ...
    @overload
    def resize(self, shape: _ShapeLike) -> None: ...
    @overload
    def resize(self, *shape: SupportsIndex) -> None: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.bool_ | np.int_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.int_: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def sum(
        self: csr_matrix[Any, Any],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.bool_ | np.int_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.int_]]: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.unsignedinteger[Any]]]: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.float_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.float_]]: ...
    @overload
    def sum(
        self: csr_matrix[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.complex_]]: ...
    @overload
    def sum(
        self: csr_matrix[Any, Any],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, Any]: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        *,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: None,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[_SCT]]: ...
    @overload
    def sum(
        self,
        axis: None,
        dtype: npt.DTypeLike,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        *,
        dtype: npt.DTypeLike = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: npt.DTypeLike,
        out: None = ...,
    ) -> np.ndarray[Any, Any]: ...
    @overload
    def sum(
        self,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex | None = ...,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        *,
        out: _ArrayType,
        dtype: npt.DTypeLike | None = ...,
    ) -> _ArrayType: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex | None,
        dtype: npt.DTypeLike | None,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def trace(
        self: csr_matrix[Any, np.dtype[np.bool_ | np.int_]],
        offset: SupportsIndex = ...,
    ) -> np.int_: ...
    @overload
    def trace(
        self: csr_matrix[Any, np.dtype[np.unsignedinteger[Any]]],
        offset: SupportsIndex = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def trace(
        self: csr_matrix[Any, np.dtype[np.float_]],
        offset: SupportsIndex = ...,
    ) -> np.float_: ...
    @overload
    def trace(
        self: csr_matrix[Any, np.dtype[np.complex_]],
        offset: SupportsIndex = ...,
    ) -> np.complex_: ...
    @overload
    def trace(self: csr_matrix[Any, Any], offset: SupportsIndex = ...) -> Any: ...
    @overload
    def todense(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def todense(self, *, out: _ArrayType) -> _ArrayType: ...
    @overload
    def todense(self, order: None, out: _ArrayType) -> _ArrayType: ...
    def tocsr(self, copy: bool = ...) -> csr_matrix[_ShapeAnno, _DType_co]: ...
    def todok(self, copy: bool = ...) -> dok_matrix[_ShapeAnno, _DType_co]: ...
    def tocoo(self, copy: bool = ...) -> coo_matrix[_ShapeAnno, _DType_co]: ...
    def tolil(self, copy: bool = ...) -> lil_matrix[_ShapeAnno, _DType_co]: ...
    def todia(self, copy: bool = ...) -> dia_matrix[_ShapeAnno, _DType_co]: ...
    def tobsr(
        self,
        blocksize: tuple[SupportsIndex, SupportsIndex] | None = ...,
        copy: bool = ...,
    ) -> bsr_matrix[_ShapeAnno, _DType_co]: ...
    def tocsc(self, copy: bool = ...) -> csc_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def mean(
        self: spmatrix[Any, np.dtype[np.bool_ | np.integer[Any] | np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def mean(
        self: spmatrix[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def mean(
        self: spmatrix[Any, Any], axis: None = ..., dtype: None = ..., out: None = ...
    ) -> Any: ...
    @overload
    def mean(
        self, axis: None = ..., *, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> _SCT: ...
    @overload
    def mean(self, axis: None, dtype: _DTypeLike[_SCT], out: None = ...) -> _SCT: ...
    @overload
    def mean(
        self, axis: None = ..., *, dtype: npt.DTypeLike, out: None = ...
    ) -> Any: ...
    @overload
    def mean(self, axis: None, dtype: npt.DTypeLike, out: None = ...) -> Any: ...
    @overload
    def mean(
        self: (
            spmatrix[Any, np.dtype[np.bool_]]
            | spmatrix[Any, np.dtype[np.integer[Any]]]
            | spmatrix[Any, np.dtype[np.float_]]
        ),
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.float_]] | np.float_: ...
    @overload
    def mean(
        self: spmatrix[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.complex_]] | np.complex_: ...
    @overload
    def mean(
        self, axis: SupportsIndex, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> np.ndarray[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex,
        dtype: npt.DTypeLike | None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def mean(
        self,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex | None = ...,
        *,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        *,
        dtype: npt.DTypeLike | None = ...,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def mean(
        self,
        axis: SupportsIndex | None,
        dtype: npt.DTypeLike | None,
        out: _ArrayType,
    ) -> _ArrayType: ...
    @overload
    def asformat(self, format: None, copy: bool = ...) -> Self: ...
    @overload
    def asformat(
        self, format: Literal["csr"], copy: bool = ...
    ) -> csr_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dok"], copy: bool = ...
    ) -> dok_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["coo"], copy: bool = ...
    ) -> coo_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["lil"], copy: bool = ...
    ) -> lil_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dia"], copy: bool = ...
    ) -> dia_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["bsr"], copy: bool = ...
    ) -> bsr_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["csc"], copy: bool = ...
    ) -> csc_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["array", "dense"]
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self,
        format: _Formats | None,
        copy: bool = ...,
    ) -> spmatrix[_ShapeAnno, _DType_co]: ...
    # In reshape, copy=False annotating is problematic, but I decided to copy from
    # numpy where it is permitted to mutate the shape without changing the ShapeType
    # typevar.
    @overload
    def reshape(
        self,
        shape: _ShapeLike,
        /,
        *,
        order: _OrderType | None = ...,
        copy: bool = ...,
    ) -> spmatrix[Any, _DType_co]: ...
    @overload
    def reshape(
        self,
        *shape: SupportsIndex,
        order: _OrderType | None = ...,
        copy: bool = ...,
    ) -> spmatrix[Any, _DType_co]: ...
    @overload
    def astype(
        self,
        dtype: _DTypeLike[_SCT],
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> csr_matrix[Any, np.dtype[_SCT]]: ...
    @overload
    def astype(
        self,
        dtype: npt.DTypeLike,
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> csr_matrix[Any, Any]: ...
    @property
    def real(self) -> csr_matrix[_ShapeAnno, Any]: ...
    @property
    def imag(self) -> csr_matrix[_ShapeAnno, Any]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: None = ...,
    ) -> csr_matrix[_ShapeAnno, Any]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: _DTypeLike[_SCT],
    ) -> csr_matrix[_ShapeAnno, np.dtype[_SCT]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: npt.DTypeLike,
    ) -> csr_matrix[_ShapeAnno, Any]: ...
    def __abs__(self) -> csr_matrix[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: csr_matrix[Any, np.dtype[np.bool_]],
        ndigits: SupportsIndex = ...,
    ) -> csr_matrix[_ShapeAnno, np.dtype[np.float16]]: ...
    @overload
    def __round__(
        self: csr_matrix[Any, np.dtype[np.complex_ | np.object_]],
        ndigits: SupportsIndex = ...,
    ) -> csr_matrix[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: csr_matrix[Any, np.dtype[_SCT_uifcO]],
        ndigits: SupportsIndex = ...,
    ) -> csr_matrix[_ShapeAnno, np.dtype[_SCT_uifcO]]: ...
    @overload
    def __round__(
        self: csr_matrix[Any, Any],
        ndigits: SupportsIndex = ...,
    ) -> csr_matrix[_ShapeAnno, Any]: ...
    # TODO: The return type of __add__ can be refined
    def __add__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __radd__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __sub__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rsub__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __matmul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rmatmul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __truediv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __div__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rtruediv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rdiv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __iadd__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __isub__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __imul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __idiv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __itruediv__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    # TODO: the type annotations of multiply, maximum, minimum and dot can be refined
    def multiply(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def maximum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def minimum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def dot(
        self, other: npt.ArrayLike | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    @property
    def T(self) -> csc_matrix[Any, _DType_co]: ...
    def transpose(
        self, axes: None = ..., copy: bool = ...
    ) -> csr_matrix[Any, _DType_co]: ...
    ###########################################################################
    # common methods/attributes from _cs_matrix
    ###########################################################################
    data: np.ndarray[Any, _DType_co]
    indices: np.ndarray[Any, np.dtype[np.int_]]
    indptr: np.ndarray[Any, np.dtype[np.int_]]
    def check_format(self, full_check: bool = ...) -> None: ...
    def eliminate_zeros(self) -> None: ...
    @property
    def has_canonical_format(self) -> bool: ...
    @has_canonical_format.setter
    def has_canonical_format(self, val: bool) -> None: ...
    def sum_duplicates(self) -> None: ...
    @property
    def has_sorted_indices(self) -> bool: ...
    @has_sorted_indices.setter
    def has_sorted_indices(self, val: _BoolLike_co) -> None: ...
    def sorted_indices(self) -> Self: ...
    def sort_indices(self) -> None: ...
    def prune(self) -> None: ...
    # input is sparse array/matrix
    @overload
    def __init__(
        self,
        arg1: sparray[Any, _DType_co] | spmatrix[Any, _DType_co],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: SparseArray[Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: SparseArray[Any],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: SparseArray[Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: SparseArray[Any],
        shape: _ShapeLike | None,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    # input is shape and dtype to init empty sparse
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[SupportsIndex, SupportsIndex],
        *,
        dtype: _DTypeLike[_SCT_co],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: tuple[SupportsIndex, SupportsIndex],
        *,
        dtype: npt.DTypeLike | None = ...,
    ) -> None: ...
    # input is data and indices
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            np.ndarray[Any, np.dtype[_SCT_co]],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: tuple[
            _ArrayLike1DDual[Any, Any],
            tuple[_ArrayLike1DIndex, _ArrayLike1DIndex],
        ],
        shape: _ShapeLike | None = ...,
        dtype: npt.DTypeLike | None = ...,
        copy: bool = ...,
    ) -> None: ...
    # input is data, indices, indptr
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[
            np.ndarray[Any, np.dtype[_SCT_co]],
            _ArrayLike1DIndex,
            _ArrayLike1DIndex,
        ],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        dtype: npt.DTypeLike | None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: np.ndarray[Any, np.dtype[_SCT_co]],
        *,
        dtype: None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csr_matrix[Any, np.dtype[_SCT_co]],
        arg1: npt.ArrayLike,
        *,
        dtype: _DTypeLike[_SCT_co],
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: npt.ArrayLike,
        *,
        dtype: npt.DTypeLike | None = ...,
    ) -> None: ...
    ###########################################################################
    # common methods from _data_matrix
    ###########################################################################
    @property
    def dtype(self) -> _DType_co: ...
    # as for ndarray, the dtype.setter is not type annotated
    def _deduped_data(self) -> np.ndarray[Any, _DType_co]: ...

    # dynamically set unary ufuncs:
    def sin(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def tan(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def arcsin(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def arctan(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def sinh(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def tanh(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def arcsinh(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def arctanh(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def rint(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def sign(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def expm1(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def log1p(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def deg2rad(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def rad2deg(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def floor(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def ceil(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def trunc(self) -> csr_matrix[_ShapeAnno, Any]: ...
    def sqrt(self) -> csr_matrix[_ShapeAnno, Any]: ...
    ###########################################################################
    # common methods from _minmax_mixin
    ###########################################################################
    @overload
    def max(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def max(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def max(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_matrix[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def max(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def min(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def min(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def min(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_matrix[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def min(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def nanmax(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def nanmax(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmax(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_matrix[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def nanmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def nanmin(self: SparseArray[_SCT], axis: None = ..., out: None = ...) -> _SCT: ...
    @overload
    def nanmin(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmin(
        self: SparseArray[_SCT], axis: SupportsIndex, out: None = ...
    ) -> coo_matrix[Any, np.dtype[_SCT]] | _SCT: ...
    @overload
    def nanmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def argmax(self, axis: None = ..., out: None = ...) -> np.int_: ...
    @overload
    def argmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> np.matrix[Any, np.dtype[np.int_]] | np.int_: ...
    @overload
    def argmin(self, axis: None = ..., out: None = ...) -> np.int_: ...
    @overload
    def argmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> np.matrix[Any, np.dtype[np.int_]] | np.int_: ...
    @property
    def format(self) -> Literal["csr"]: ...
