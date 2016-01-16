# Pweave documentation

This repository holds Pweave documentation sources. You can find the latest published docs from http://mpastell.com/pweave.

## Contributing to the docs

Contributions to the docs are very welcome in order to keep them up to date!
The docs are generated from files in the `pweave_source` and `examples directory`. Be careful to make changes there and not in the `source` directory for the relevant files (check `run_pweave.sh` for files generating output to `source`).

Build the docs using:

```
./run_pweave.sh
make html
```
and commit the relevant changed files and everything from `source` directory to git.
