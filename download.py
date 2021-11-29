import os
from pathlib import Path, PurePath
import sys

import datasets

def ensure_dir(path):
    print("ensure", path)
    try:
        os.makedirs(path)
    except FileExistsError:
        pass # dir already exists

def ensure_matrix_download(dir, mat):
    if os.path.exists(dir / mat.name / (mat.name + ".mtx")):
        print(f"SKIP {mat.name}: already exists")
        return
    mat.download(format='MM', destpath=dir, extract=True)

# create a link in linkDir for the matrix in downDir
def ensure_matrix_link(downDir, linkDir, mat):
    files = os.listdir(downDir / mat.name)
    for f in files:
        if f == mat.name + ".mtx":
            # os.path.relpath does not require one to be a subpath of the other
            src = Path(os.path.relpath(downDir, linkDir)) / mat.name / f
            dst = linkDir / (mat.name + ".mtx")
            print(f"{src} <- {dst}")
            try:
                os.symlink(src, dst)
            except FileExistsError:
                pass # dir already exists
            return

def download_dataset(dataset):
    mats = dataset.mats

    print(len(mats))

    # scratch directory
    scratchPath = Path(os.environ["SCRATCH"])
    # where matrices will be downloaded
    downDir = scratchPath / "suitesparse"
    # where the matrix will be linked to
    linkDir = scratchPath / dataset.name
    ensure_dir(downDir)
    ensure_dir(linkDir)

    for mat in mats:
        print(mat.name)
        ensure_matrix_download(downDir, mat)
        ensure_matrix_link(downDir, linkDir, mat)

if "all" == sys.argv[1]:
    for ds in datasets.DATASETS:
        download_dataset(ds)
    sys.exit(0)
else:
    dataset = None
    for ds in datasets.DATASETS:
        if ds.name == sys.argv[1]:
            download_dataset(ds)
            sys.exit(0)
