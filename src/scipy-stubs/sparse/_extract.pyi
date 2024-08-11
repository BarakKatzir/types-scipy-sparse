from typing import Any, Literal, SupportsIndex, overload

import numpy as np
import numpy.typing as npt

from ._base import sparray
from ._bsr import bsr_array, bsr_matrix
from ._coo import coo_array, coo_matrix
from ._csc import csc_array, csc_matrix
from ._csr import csr_array, csr_matrix
from ._dia import dia_array, dia_matrix
from ._dok import dok_array, dok_matrix
from ._lil import lil_array, lil_matrix
from ._matrix import spmatrix
from .typing import _SCT, SparseArray

__all__ = ["find", "tril", "triu"]

@overload
def find(
    A: SparseArray[_SCT] | np.ndarray[Any, np.dtype[_SCT]],
) -> tuple[
    np.ndarray[Any, np.dtype[np.int_]],
    np.ndarray[Any, np.dtype[np.int_]],
    np.ndarray[Any, np.dtype[_SCT]],
]: ...
@overload
def find(
    A: SparseArray[Any] | npt.ArrayLike,
) -> tuple[
    np.ndarray[Any, np.dtype[np.int_]],
    np.ndarray[Any, np.dtype[np.int_]],
    np.ndarray[Any, Any],
]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    format: Literal["coo"] | None = ...,
) -> coo_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    format: Literal["coo"] | None = ...,
) -> coo_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    format: Literal["coo"] | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dia"],
) -> dia_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dia"],
) -> dia_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT]]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def tril(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    format: Literal["coo"] | None = ...,
) -> coo_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    format: Literal["coo"] | None = ...,
) -> coo_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    format: Literal["coo"] | None = ...,
) -> coo_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csc"],
) -> csc_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["csc"],
) -> csc_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csr"],
) -> csr_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["csr"],
) -> csr_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["bsr"],
) -> bsr_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["bsr"],
) -> bsr_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dia"],
) -> dia_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dia"],
) -> dia_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["dia"],
) -> dia_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dok"],
) -> dok_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["dok"],
) -> dok_matrix[Any, Any]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: sparray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["lil"],
) -> lil_array[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex,
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: spmatrix[Any, np.dtype[_SCT]] | np.ndarray[Any, np.dtype[_SCT]],
    k: SupportsIndex = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, np.dtype[_SCT]]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
@overload
def triu(
    A: npt.ArrayLike,
    k: SupportsIndex = ...,
    *,
    format: Literal["lil"],
) -> lil_matrix[Any, Any]: ...
