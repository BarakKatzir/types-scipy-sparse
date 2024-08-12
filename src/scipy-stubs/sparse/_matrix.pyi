from collections.abc import Iterator
from typing import (
    Any,
    Literal,
    Protocol,
    SupportsIndex,
    overload,
    runtime_checkable,
)
from typing_extensions import Self

import numpy as np
import numpy.typing as npt

from ._bsr import bsr_matrix
from ._coo import coo_matrix
from ._csc import csc_matrix
from ._csr import csr_matrix
from ._dia import dia_matrix
from ._dok import dok_matrix
from ._lil import lil_matrix
from .typing import (
    _SCT,
    SparseArray,
    _ArrayType,
    _CastingKind,
    _DType_co,
    _DTypeLike,
    _Formats,
    _IntLike_co,
    _NumberLike_co,
    _OrderType,
    _SCT_uifcO,
    _ShapeAnno,
    _ShapeLike,
)

# Although spmatrix is not a Protocol, I hint it as such such that if
# subclassed it is clear that the methods and attributes are meant to be
# implemented. All methods and attributes are as in the private base class
# _spbase (except for the missing `def __init__`)
@runtime_checkable
class spmatrix(Protocol[_ShapeAnno, _DType_co]):
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
        self: spmatrix[Any, np.dtype[np.bool_ | np.int_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.int_: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.float_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.float_: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.complex_]],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> np.complex_: ...
    @overload
    def sum(
        self: spmatrix[Any, Any],
        axis: None = ...,
        dtype: None = ...,
        out: None = ...,
    ) -> Any: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.bool_ | np.int_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.int_]]: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.unsignedinteger[Any]]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.unsignedinteger[Any]]]: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.float_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.float_]]: ...
    @overload
    def sum(
        self: spmatrix[Any, np.dtype[np.complex_]],
        axis: SupportsIndex,
        dtype: None = ...,
        out: None = ...,
    ) -> np.ndarray[Any, np.dtype[np.complex_]]: ...
    @overload
    def sum(
        self: spmatrix[Any, Any],
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
        self: spmatrix[Any, np.dtype[np.bool_ | np.int_]],
        offset: SupportsIndex = ...,
    ) -> np.int_: ...
    @overload
    def trace(
        self: spmatrix[Any, np.dtype[np.unsignedinteger[Any]]],
        offset: SupportsIndex = ...,
    ) -> np.unsignedinteger[Any]: ...
    @overload
    def trace(
        self: spmatrix[Any, np.dtype[np.float_]],
        offset: SupportsIndex = ...,
    ) -> np.float_: ...
    @overload
    def trace(
        self: spmatrix[Any, np.dtype[np.complex_]],
        offset: SupportsIndex = ...,
    ) -> np.complex_: ...
    @overload
    def trace(self: spmatrix[Any, Any], offset: SupportsIndex = ...) -> Any: ...
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
    ) -> spmatrix[Any, np.dtype[_SCT]]: ...
    @overload
    def astype(
        self,
        dtype: npt.DTypeLike,
        casting: _CastingKind = ...,
        copy: bool = ...,
    ) -> spmatrix[Any, Any]: ...
    @property
    def real(self) -> spmatrix[_ShapeAnno, Any]: ...
    @property
    def imag(self) -> spmatrix[_ShapeAnno, Any]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: None = ...,
    ) -> spmatrix[_ShapeAnno, Any]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: _DTypeLike[_SCT],
    ) -> spmatrix[_ShapeAnno, np.dtype[_SCT]]: ...
    @overload
    def power(
        self,
        n: _NumberLike_co,
        dtype: npt.DTypeLike,
    ) -> spmatrix[_ShapeAnno, Any]: ...
    def __abs__(self) -> spmatrix[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: spmatrix[Any, np.dtype[np.bool_]],
        ndigits: SupportsIndex = ...,
    ) -> spmatrix[_ShapeAnno, np.dtype[np.float16]]: ...
    @overload
    def __round__(
        self: spmatrix[Any, np.dtype[np.complex_ | np.object_]],
        ndigits: SupportsIndex = ...,
    ) -> spmatrix[_ShapeAnno, Any]: ...
    @overload
    def __round__(
        self: spmatrix[Any, np.dtype[_SCT_uifcO]],
        ndigits: SupportsIndex = ...,
    ) -> spmatrix[_ShapeAnno, np.dtype[_SCT_uifcO]]: ...
    @overload
    def __round__(
        self: spmatrix[Any, Any],
        ndigits: SupportsIndex = ...,
    ) -> spmatrix[_ShapeAnno, Any]: ...
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
    def T(self) -> spmatrix[Any, _DType_co]: ...
    def transpose(
        self, axes: None = ..., copy: bool = ...
    ) -> spmatrix[Any, _DType_co]: ...
    @property
    def format(self) -> str: ...

    ###########################################################################
    # _matrix methods that override _spbase def
    ###########################################################################
    def __mul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __rmul__(
        self, other: np.ndarray[Any, Any] | SparseArray[Any]
    ) -> np.ndarray[Any, Any] | SparseArray[Any]: ...
    def __pow__(self, power: _IntLike_co) -> spmatrix[Any, Any]: ...

    ###########################################################################
    # spmatrix only methods
    ###########################################################################
    def set_shape(self, shape: tuple[SupportsIndex, SupportsIndex]) -> None: ...
    def get_shape(self) -> tuple[int, int]: ...
    # The shape.setter is not annotated (similar to np.ndarray)
    def asfptype(self) -> spmatrix[Any, Any]: ...
    def getmaxprint(self) -> int: ...
    def getformat(self) -> _Formats: ...
    @overload
    def getnnz(self, axis: None = ...) -> int: ...
    @overload
    def getnnz(self, axis: SupportsIndex) -> np.ndarray[Any, np.dtype[np.int_]]: ...
    def getH(self) -> spmatrix[Any, _DType_co]: ...
    def getcol(self, j: SupportsIndex) -> spmatrix[Any, _DType_co]: ...
    def getrow(self, i: SupportsIndex) -> spmatrix[Any, _DType_co]: ...
