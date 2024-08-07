from collections.abc import Iterator
from typing import Any, Literal, SupportsIndex, overload
from typing_extensions import Self, TypeIs

import numpy as np
import numpy.typing as npt

from ._base import sparray
from ._bsr import bsr_array, bsr_matrix
from ._coo import coo_array, coo_matrix
from ._csr import csr_array, csr_matrix
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

__all__ = ["csc_array", "csc_matrix", "isspmatrix_csc"]

def isspmatrix_csc(x: Any) -> TypeIs[csc_matrix[Any, Any]]: ...

class csc_array(sparray[_ShapeAnno, _DType_co], IndexMixin):
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
    def nonzero(self) -> tuple[npt.NDArray[np.int_], npt.NDArray[np.int_]]: ...
    @overload
    def toarray(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def toarray(self, order: None = ..., out: _ArrayType = ...) -> _ArrayType: ...
    def copy(self) -> Self: ...
    def diagonal(self, k: SupportsIndex = ...) -> np.ndarray[Any, _DType_co]: ...
    def setdiag(self, values: npt.ArrayLike, k: SupportsIndex = ...) -> None: ...
    @overload
    def resize(self, shape: _ShapeLike) -> None: ...
    @overload
    def resize(self, *shape: SupportsIndex) -> None: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.bool_ | np.int_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.int_: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.bool_ | np.int_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.unsignedinteger[Any]]: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.float_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.float_]: ...
    @overload
    def sum(
        self: csc_array[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.complex_]: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[Any]: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        dtype: _DTypeLike[_SCT] = ...,
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> npt.NDArray[_SCT]: ...
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
    ) -> npt.NDArray[Any]: ...
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
        self: csc_array[Any, np.dtype[np.bool_ | np.int_]],
        offset: SupportsIndex = ...,
    ) -> np.int_: ...
    @overload
    def trace(
        self: csc_array[Any, np.dtype[np.unsignedinteger[Any]]],
        offset: SupportsIndex = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def trace(
        self: csc_array[Any, np.dtype[np.float_]],
        offset: SupportsIndex = ...,
    ) -> np.float_: ...
    @overload
    def trace(
        self: csc_array[Any, np.dtype[np.complex_]],
        offset: SupportsIndex = ...,
    ) -> np.complex_: ...
    @overload
    def trace(self, offset: SupportsIndex = ...) -> Any: ...
    @overload
    def todense(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def todense(self, *, out: _ArrayType = ...) -> _ArrayType: ...
    @overload
    def todense(self, order: None, out: _ArrayType = ...) -> _ArrayType: ...
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
        self: (
            sparray[Any, np.dtype[np.bool_]]
            | sparray[Any, np.dtype[np.integer[Any]]]
            | sparray[Any, np.dtype[np.float_]]
        ),
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
    def mean(self, axis: None = ..., dtype: None = ..., out: None = ...) -> Any: ...
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
    ) -> npt.NDArray[np.float_] | np.float_: ...
    @overload
    def mean(
        self: sparray[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.complex_] | np.complex_: ...
    @overload
    def mean(
        self, axis: SupportsIndex, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> npt.NDArray[_SCT] | _SCT: ...
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
    # In asformat, copy=False is not Type annotated, though is valid runtime value.
    # This is because the dynamic type change is not compatible with static type
    # checker.
    @overload
    def asformat(self, format: None, copy: bool) -> Self: ...
    @overload
    def asformat(
        self, format: Literal["csr"], copy: Literal[True]
    ) -> csr_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dok"], copy: Literal[True]
    ) -> dok_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["coo"], copy: Literal[True]
    ) -> coo_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["lil"], copy: Literal[True]
    ) -> lil_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dia"], copy: Literal[True]
    ) -> dia_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["bsr"], copy: Literal[True]
    ) -> bsr_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["csc"], copy: Literal[True]
    ) -> csc_array[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["array", "dense"]
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self,
        format: _Formats | None,
        copy: Literal[True],
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
    ) -> csc_array[Any, np.dtype[_SCT]]: ...
    @overload
    def astype(
        self,
        dtype: npt.DTypeLike,
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> csc_array[Any, Any]: ...
    @property
    def real(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    @property
    def imag(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: None = ...,
    ) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: _DTypeLike[_SCT],
    ) -> csc_array[_ShapeAnno, np.dtype[_SCT]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: npt.DTypeLike,
    ) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def __abs__(self) -> csc_array[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: csc_array[Any, np.dtype[np.bool_]],
        ndigits: SupportsIndex = ...,
    ) -> csc_array[_ShapeAnno, np.dtype[np.float16]]: ...
    @overload
    def __round__(
        self: csc_array[Any, np.dtype[np.complex_ | np.object_]],
        ndigits: SupportsIndex = ...,
    ) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def __round__(
        self: csc_array[Any, np.dtype[_SCT_uifcO]],
        ndigits: SupportsIndex = ...,
    ) -> csc_array[_ShapeAnno, np.dtype[_SCT_uifcO]]: ...
    @overload
    def __round__(
        self,
        ndigits: SupportsIndex = ...,
    ) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    # TODO: The return type here can be refined
    def __add__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __radd__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __sub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rsub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __matmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rmatmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __truediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __div__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rtruediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rdiv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __iadd__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __isub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __imul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __idiv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __itruediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...

    # TODO: the `T` and `transpose` methods need refinement.csc -> csr anything else?
    # Despite T and transpose (if copy=False) by default mutate the shape of self, and
    # can cause incompatibility with the ShapeType variable, I followed numpy's
    # approach and allowed this.
    @property
    def T(self) -> sparray[Any, _DType_co]: ...
    def transpose(
        self, axes: None = ..., copy: bool = ...
    ) -> sparray[Any, _DType_co]: ...
    # TODO: the type annotations of multiply, maximum, minimum and dot can be refined by
    # defining them per-final sparse class, but for now I leave them quite general
    def multiply(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def maximum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def minimum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def dot(
        self, other: npt.ArrayLike | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    ###########################################################################
    # __init__ of _cs_matrix
    ###########################################################################
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
        self: csc_array[Any, np.dtype[_SCT_co]],
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    # input is shape and dtype to init empty sparse
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
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
        self: csc_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[npt.NDArray[_SCT_co], tuple[_ArrayLike1DIndex, _ArrayLike1DIndex]],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
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
        self: csc_array[Any, np.dtype[_SCT_co]],
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
        self: csc_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[npt.NDArray[_SCT_co], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
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
    # input is array
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
        arg1: npt.NDArray[_SCT_co],
        *,
        dtype: None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_array[Any, np.dtype[_SCT_co]],
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
    # common methods/attributes from _cs_matrix
    ###########################################################################
    data: np.ndarray[Any, _DType_co]
    indices: npt.NDArray[np.int_]
    indptr: npt.NDArray[np.int_]
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
    ###########################################################################
    # common methods from _data_matrix
    ###########################################################################
    @property
    def dtype(self) -> _DType_co: ...
    # as for ndarray, the dtype.setter is not type annotated
    def _deduped_data(self) -> np.ndarray[Any, _DType_co]: ...

    # dynamically set unary ufuncs:
    def sin(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def tan(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def arcsin(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def arctan(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def sinh(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def tanh(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def arcsinh(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def arctanh(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def rint(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def sign(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def expm1(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def log1p(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def deg2rad(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def rad2deg(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def floor(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def ceil(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def trunc(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    def sqrt(self) -> csc_array[_ShapeAnno, np.dtype[Any]]: ...
    ###########################################################################
    # common methods from _minmax_mixin
    ###########################################################################
    # TODO: is this return type correct? no coo_array?
    @overload
    def max(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def max(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def min(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def min(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def nanmax(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def nanmin(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def argmax(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def argmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def argmin(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def argmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @property
    def format(self) -> Literal["csc"]: ...

class csc_matrix(spmatrix[_ShapeAnno, _DType_co], IndexMixin):
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
    def nonzero(self) -> tuple[npt.NDArray[np.int_], npt.NDArray[np.int_]]: ...
    @overload
    def toarray(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def toarray(self, order: None = ..., out: _ArrayType = ...) -> _ArrayType: ...
    def copy(self) -> Self: ...
    def diagonal(self, k: SupportsIndex = ...) -> np.ndarray[Any, _DType_co]: ...
    def setdiag(self, values: npt.ArrayLike, k: SupportsIndex = ...) -> None: ...
    @overload
    def resize(self, shape: _ShapeLike) -> None: ...
    @overload
    def resize(self, *shape: SupportsIndex) -> None: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.bool_ | np.int_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.int_: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.bool_ | np.int_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.unsignedinteger[Any]]: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.float_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.float_]: ...
    @overload
    def sum(
        self: csc_matrix[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.complex_]: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[Any]: ...
    @overload
    def sum(
        self,
        axis: None = ...,
        dtype: _DTypeLike[_SCT] = ...,
        out: None = ...,
    ) -> _SCT: ...
    @overload
    def sum(
        self,
        axis: SupportsIndex,
        dtype: _DTypeLike[_SCT],
        out: None = ...,
    ) -> npt.NDArray[_SCT]: ...
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
    ) -> npt.NDArray[Any]: ...
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
        self: csc_matrix[Any, np.dtype[np.bool_ | np.int_]],
        offset: SupportsIndex = ...,
    ) -> np.int_: ...
    @overload
    def trace(
        self: csc_matrix[Any, np.dtype[np.unsignedinteger[Any]]],
        offset: SupportsIndex = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def trace(
        self: csc_matrix[Any, np.dtype[np.float_]],
        offset: SupportsIndex = ...,
    ) -> np.float_: ...
    @overload
    def trace(
        self: csc_matrix[Any, np.dtype[np.complex_]],
        offset: SupportsIndex = ...,
    ) -> np.complex_: ...
    @overload
    def trace(self, offset: SupportsIndex = ...) -> Any: ...
    @overload
    def todense(
        self, order: _OrderType | None = ..., out: None = ...
    ) -> np.matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def todense(self, *, out: _ArrayType = ...) -> _ArrayType: ...
    @overload
    def todense(self, order: None, out: _ArrayType = ...) -> _ArrayType: ...
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
        self: (
            spmatrix[Any, np.dtype[np.bool_]]
            | spmatrix[Any, np.dtype[np.integer[Any]]]
            | spmatrix[Any, np.dtype[np.float_]]
        ),
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
    def mean(self, axis: None = ..., dtype: None = ..., out: None = ...) -> Any: ...
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
    ) -> npt.NDArray[np.float_] | np.float_: ...
    @overload
    def mean(
        self: spmatrix[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> npt.NDArray[np.complex_] | np.complex_: ...
    @overload
    def mean(
        self, axis: SupportsIndex, dtype: _DTypeLike[_SCT], out: None = ...
    ) -> npt.NDArray[_SCT] | _SCT: ...
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
    # In asformat, copy=False is not Type annotated, though is valid runtime value.
    # This is because the dynamic type change is not compatible with static type
    # checker.
    @overload
    def asformat(self, format: None, copy: bool) -> Self: ...
    @overload
    def asformat(
        self, format: Literal["csr"], copy: Literal[True]
    ) -> csr_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dok"], copy: Literal[True]
    ) -> dok_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["coo"], copy: Literal[True]
    ) -> coo_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["lil"], copy: Literal[True]
    ) -> lil_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["dia"], copy: Literal[True]
    ) -> dia_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["bsr"], copy: Literal[True]
    ) -> bsr_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["csc"], copy: Literal[True]
    ) -> csc_matrix[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self, format: Literal["array", "dense"]
    ) -> np.ndarray[_ShapeAnno, _DType_co]: ...
    @overload
    def asformat(
        self,
        format: _Formats | None,
        copy: Literal[True],
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
    ) -> csc_matrix[Any, np.dtype[_SCT]]: ...
    @overload
    def astype(
        self,
        dtype: npt.DTypeLike,
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> csc_matrix[Any, Any]: ...
    @property
    def real(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    @property
    def imag(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: None = ...,
    ) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: _DTypeLike[_SCT],
    ) -> csc_matrix[_ShapeAnno, np.dtype[_SCT]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: npt.DTypeLike,
    ) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def __abs__(self) -> csc_matrix[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: csc_matrix[Any, np.dtype[np.bool_]],
        ndigits: SupportsIndex = ...,
    ) -> csc_matrix[_ShapeAnno, np.dtype[np.float16]]: ...
    @overload
    def __round__(
        self: csc_matrix[Any, np.dtype[np.complex_ | np.object_]],
        ndigits: SupportsIndex = ...,
    ) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    @overload
    def __round__(
        self: csc_matrix[Any, np.dtype[_SCT_uifcO]],
        ndigits: SupportsIndex = ...,
    ) -> csc_matrix[_ShapeAnno, np.dtype[_SCT_uifcO]]: ...
    @overload
    def __round__(
        self,
        ndigits: SupportsIndex = ...,
    ) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    # TODO: The return type here can be refined
    def __add__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __radd__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __sub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rsub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __matmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rmatmul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __truediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __div__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rtruediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __rdiv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __iadd__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __isub__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __imul__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __idiv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    def __itruediv__(
        self, other: npt.NDArray[Any] | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...

    # TODO: the `T` and `transpose` methods need refinement.csc -> csr anything else?
    # Despite T and transpose (if copy=False) by default mutate the shape of self, and
    # can cause incompatibility with the ShapeType variable, I followed numpy's
    # approach and allowed this.
    @property
    def T(self) -> spmatrix[Any, _DType_co]: ...
    def transpose(
        self, axes: None = ..., copy: bool = ...
    ) -> spmatrix[Any, _DType_co]: ...
    # TODO: the type annotations of multiply, maximum, minimum and dot can be refined by
    # defining them per-final sparse class, but for now I leave them quite general
    def multiply(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def maximum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def minimum(self, other: npt.ArrayLike | SparseArray[Any]) -> SparseArray[Any]: ...
    def dot(
        self, other: npt.ArrayLike | SparseArray[Any]
    ) -> npt.NDArray[Any] | SparseArray[Any]: ...
    ###########################################################################
    # __init__ of _cs_matrix
    ###########################################################################
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
        self: csc_matrix[Any, np.dtype[_SCT_co]],
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None = ...,
        *,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        arg1: sparray[Any, Any] | spmatrix[Any, Any],
        shape: _ShapeLike | None,
        dtype: npt.DTypeLike,
        copy: bool = ...,
    ) -> None: ...
    # input is shape and dtype to init empty sparse
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
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
        self: csc_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[npt.NDArray[_SCT_co], tuple[_ArrayLike1DIndex, _ArrayLike1DIndex]],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
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
        self: csc_matrix[Any, np.dtype[_SCT_co]],
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
        self: csc_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[npt.NDArray[_SCT_co], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        dtype: None = ...,
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
        arg1: tuple[_ArrayLike1DDual[Any, Any], _ArrayLike1DIndex, _ArrayLike1DIndex],
        shape: _ShapeLike | None = ...,
        *,
        dtype: _DTypeLike[_SCT_co],
        copy: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
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
    # input is array
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
        arg1: npt.NDArray[_SCT_co],
        *,
        dtype: None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: csc_matrix[Any, np.dtype[_SCT_co]],
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
    # common methods/attributes from _cs_matrix
    ###########################################################################
    data: np.ndarray[Any, _DType_co]
    indices: npt.NDArray[np.int_]
    indptr: npt.NDArray[np.int_]
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
    ###########################################################################
    # common methods from _data_matrix
    ###########################################################################
    @property
    def dtype(self) -> _DType_co: ...
    # as for ndarray, the dtype.setter is not type annotated
    def _deduped_data(self) -> np.ndarray[Any, _DType_co]: ...

    # dynamically set unary ufuncs:
    def sin(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def tan(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def arcsin(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def arctan(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def sinh(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def tanh(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def arcsinh(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def arctanh(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def rint(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def sign(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def expm1(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def log1p(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def deg2rad(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def rad2deg(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def floor(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def ceil(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def trunc(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    def sqrt(self) -> csc_matrix[_ShapeAnno, np.dtype[Any]]: ...
    ###########################################################################
    # common methods from _minmax_mixin
    ###########################################################################
    # TODO: is this return type correct? no coo_array?
    @overload
    def max(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def max(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def min(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def min(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def nanmax(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def nanmin(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def nanmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def argmax(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def argmax(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @overload
    def argmin(self, axis: None = ..., out: None = ...) -> np.number[Any]: ...
    @overload
    def argmin(
        self, axis: SupportsIndex, out: None = ...
    ) -> coo_matrix | np.number[Any]: ...
    @property
    def format(self) -> Literal["csc"]: ...
