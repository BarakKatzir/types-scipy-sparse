# Development of `types-scipy-sparse`

I list here some details regarding developing this package and some other miscellaneous topics.

## Annotated private API

This pacakges avoids adding types to the internal private functionality of `scipy.sparse`, but there are some exceptions:

* the function `_todata` and function `_ravel_coords` that seems useful and well docstringed.

* the whole *private* module `scipy.sparse._sparsetools` is not exposed in `__init__.py`, but some of its functions are re-exposed by some deprecated modules such as `bsr.py`, `compressed.py`, `construct.py` and some others.

## Testing

The package is tested by:

1) The package passes `ruff` checks

2) Stubs checked with `mypy`

3) Stubs checked with `stubtest`

4) Testing for mypy failure/pass/reveals - adapted from the now archived, `numpy-stubs` package (see https://github.com/numpy/numpy-stubs).

## Common stub generation

The scipy sparse module has a lot of annotations that need repeating for the different sparse arrays / matrices.
To save myself time, and to avoid copy-paste errors, A convenience tool generates some of the stub files.
The tool is located in the `make-scipy-sparse-stubs` folder and contains the python script `make_scipy_sparse_stubs.py`

Examples for usage:

```shell
$ python -m make_scipy_sparse_stubs -c
Finished without any changes 🎉
```

or to overwrite the current stubs by specifying their location in the workspace

```shell
$ python -m make_scipy_sparse_stubs -sp src/scipy-stubs
Finished without any changes 🎉
```

## Development environment

To develop locally follow the following steps:

1) clone the package

2) [install uv](https://docs.astral.sh/uv/installation/)

3) In workspace root, create virtual environment

  ```bash
  $ uv venv -p 3.10
  ```

  and activate the venv

4) now install the package and its dependencies and dev-dependencies

  ```bash
  $ uv sync
  ```

5) for the stubs to work you need to install in non-editable mode for some reason

  ```bash
  $ uv pip install .
  ```

## Completion list of stubs in `scipy.sparse` module

Here is a list of modules and classes that plan to type or have typed already:

```terminal
├── sparse
├── [V] __init__.pyi
├── [V] _base.pyi
├── [V] _bsr.pyi
├── [X] _compressed.pyi  (private)
├── [V] _construct.pyi
├── [V] _coo.pyi
├── [V] _csc.pyi
├── [V] _csr.pyi
├── [V] _data.pyi
├── [V] _dia.pyis
├── [V] _dok.pyi
├── [V] _extract.pyi
├── [X] _generate_sparsetools.pyi  (private)
├── [X] _csparsetools.pyi  (private)
├── [V] _sparsetools.pyi  (private but leaks outside via depracated modules)
├── [V] _index.pyi
├── [V] _lil.pyi
├── [V] _matrix.pyi
├── [V] _matrix_io.pyi
├── [X] _spfuncs.pyi  (private)
├── [V] _sputils.pyi
├── [V] base.pyi
├── [V] bsr.pyi
├── [V] compressed.pyi
├── [V] construct.pyi
├── [V] coo.pyi
├── [V] csc.pyi
├── [V] csr.pyi
├── [V] data.pyi
├── [V] dia.pyi
├── [V] dok.pyi
├── [V] extract.pyi
├── [V] lil.pyi
├── [V] sparsetools.pyi
├── [V] spfuncs.pyi
├── [V] sputils.pyi
├── csgraph
|   ├── [ ] __init__.pyi
|   └── ...
└── linalg
    ├── [ ] __init__.pyi
    └── ...
```
