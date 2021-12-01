# ss-downloader

Install poetry & Python 3.8+

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## how to use

```
source load-env.sh
poetry run python list.py
poetry run python download.py <dataset name>
```

To download all datasets
```
poetry run python download.py all
```

You can move the datasets due to relative symlinks. For example:

```
rsync -azvh $SCRATCH/ ~/cfm_m3918/pearson
```

## how to use (unsupported platform)

set `SS_DIR` environment variable to the directory where you want the dataset folders to be generated.

## What it does

Downloads subsets of the suitesparse collection to different directories.
For a given subset, the matrices are first downloaded to the `$SCRATCH/suitesparse` folder. If a required matrix already exists there, it is not redownloaded.
Then, a relative symlink is created from the `$SCRATCH/<subset>/<matrix>.mtx` file to the corresponding `.mtx` file in `$SCRATCH/suitesparse`.

This makes use of a [fork of the `ssgetpy`](github.com/cwpearson/ssgetpy) package with a faster download limit.
ssgetpy does not discriminate "real" datatype from "integer" datatype, as shown on the suitesparse collection website.
Therefore, `lists.py` maintains a manually-curated list of `integer` datatype matrices to facilitate discrimination.

## Transfer data to a different filesystem

```
rsync -rzvh --links pearson@cori.nersc.gov:$SS_DIR/ .
```

## how this was done

```
poetry-new init
poetry add ssgetpy
```

```
poetry install
```
