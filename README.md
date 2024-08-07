# Type annotations stubs for `scipy.sparse`

This is a [PEP-561](https://peps.python.org/pep-0561/) compilant type information package for the `sparse` module of the [`SciPy`](https://scipy.org/) package.
Installing this package will allow [`mypy`](https://mypy.readthedocs.io/en/latest/installed_packages.html) and possibly other static type checkers (e.g., pyright) to recognize type annotations for `scipy.sparse` classes and functions.

> __NOTE__ :
>
> This package is a work in progress and not all annotations are tested.
>
> Currently the `csgraph` and `linalg` submodules are not type annotated.
>
> This package only supports `"numpy <2.0.0"` for now.

## Installation

In your python environment run

```bash
pip install types-scipy-sparse
```

## Annotations

The basic annotations work fine. For example, if we have the file `important_func.py` with content

```python
from scipy.sparse import coo_array

def make_sparse(
    x: list[int], y: list[int], vals: list[float]
) -> csr_array:
    return coo_array((vals, (x, y))).tocsr()

```

it will pass a mypy check

```console
$ mypy important_func.py
Success: no issues found in 1 source file
```

### Type narrowing functions

There are several convenience type-narrowing functions in the `sparse` module, e.g., `issparse`, `isspmatrix` and `isdense`. These are annotated with the `TypeIs` introduced in [PEP-742](https://peps.python.org/pep-0742/). This conveniently narrows the type (and not casts to it, like `typing.TypeGuard`) and allows type narrowing in both `if` and `else` branches of a conditional.

For example if the content of `my_script.py` is

```python
from typing import Any
from scipy.sparse import csr_array, issparse
import numpy as np

x: np.ndarray[Any, Any] | csr_array
reveal_type(x)
if issparse(x):
    reveal_type(x)
    x.indptr
elif isinstance(x, np.ndarray):
    reveal_type(x)
else:
    # This branch is inferred to be unreachable
    # so type checkers ignore the following
    b"hello" + "world!!" / 3.1

```

Then mypy will correctly infer the types in all branches

```console
$ mypy my_script.py
my_script.py:7: note: Revealed type is "scipy.sparse._csr.csr_array[Any, numpy.dtype[Any]]"
my_script.py:10: note: Revealed type is "numpy.ndarray[Any, Any]"
Success: no issues found in 1 source file
```

### `numpy`-flavored generics

The different sparse array and sparse matrix classes are type annotated similarly to `numpy.ndarray`s, with two `TypeVar`s: `<sparse_class>[ShapeType, DType]`, for example `csc_array[Any, np.float32]`. As in `ndarray`s, the `DType` is bound by `numpy.dtype[Any]` and the `ShapeType` can be anything.

For example, if the content of `important_script.py` is

```python
from scipy.sparse import csr_array, lil_array
import numpy as np

x = csr_array([[0, 1], [2, 0]], dtype=np.float64)
reveal_type(x)
y = lil_array(np.array([[0, 1], [2, 0]], dtype=np.float32))
reveal_type(y)

```

then mypy will infer correctly the `DType` of the `x` and `y` arrays

```console
$ mypy important_script.py
important_script.py:5: note: Revealed type is "scipy.sparse._csr.csr_array[Any, numpy.dtype[numpy.floating[numpy._typing._64Bit]]]"
important_script.py:7: note: Revealed type is "scipy.sparse._lil.lil_array[Any, numpy.dtype[numpy.floating[numpy._typing._32Bit]]]"
Success: no issues found in 1 source file
```

As in numpy, the first typevar, `ShapeType`, is left for user customization.

Note that for compatibility with any previous type stub packages, The `ShapeType` and `DType` typevars are the ShapeType and Dtype default to `Any`, using the [PEP-696](https://peps.python.org/pep-0696/) feature. This means that type annotating

```python
x: dok_array
```

implicitly insert these `Any`s

```console
$ mypy -c "import scipy.sparse as sp; x: sp.dok_array; reveal_type(x)"
<string>:1: note: Revealed type is "scipy.sparse._dok.dok_array[Any, numpy.dtype[Any]]"
Success: no issues found in 1 source file
```

**However**, since these generics are only introduced in the type stubs, they will raise an error at runtime. If you desire to use this feature, there are two easy solutions. The first is to use implicit forward references by adding `from __future__ import annotations` at the top of your script. The second is to explicitly use forward references by putting the troublesome annotations in quotation marks as `x: "coo_array[Any, np.uint8]"`.

### The `sparray` and `spmatrix` namespace classes

The `sparray` (and the soon to be deprecated `spmatrix`) is a class with an empty body used for namespacing and `isinstance` checks, while the many sparse array/matrix class' methods are implemented via private mixin classes. While the private classes are not type annotated by this package, the sparray and spmatrix are conveniantly type annotated as `Protocol[ShapeType, DType]`, this way it is conveyed to the type-checker that any methods they carry (such as `sum` and `asformat`) are not implemented.


### New `scipy.sparse.typing`

This type package introduces a new module for convenience. It uses it internally for common type aliases but exposes the `SparseArray` type alias which can specify some sparse array or sparse matrix by its scalar type (e.g., `np.int8` and `np.complex128`),

```python
_SCT_co = TypeVar("_SCT_co", covariant=True, bound=np.generic)
SparseArray: TypeAlias = (
    sparray[Any, np.dtype[_SCT_co]]
    | spmatrix[Any, np.dtype[_SCT_co]]
)
```

For example, the following passes mypy

```python
from __future__ import annotations

from typing import TYPE_CHECKING
import numpy as np
if TYPE_CHECKING:
    from scipy.sparse.typing import SparseArray

def foo(x: SparseArray[np.float64]) -> None:
    print(f"doing serious calculations with {x}")

```
