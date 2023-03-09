# ss-downloader

```
pipenv shell
pip install -r requirements.txt
```

## how to use

```
source load-env.sh
python list.py
python download.py <dataset name>
```

To download all datasets
```
python download.py all
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
Therefore, we access https://sparse.tamu.edu/files/ss_index.mat to determine that metadata for each file.

## Transfer data to a different filesystem

```
rsync -rzvh --links --info=progress2 pearson@cori.nersc.gov:$SS_DIR/ .
```

## how this was done

```
poetry-new init
poetry add ssgetpy
```

```
poetry install
```
