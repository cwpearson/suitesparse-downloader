import os
from pathlib import Path
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

# link matrix in downDir to linkDir
def ensure_matrix_link(downDir, linkDir, mat):
    files = os.listdir(downDir / mat.name)
    for f in files:
        if f == mat.name + ".mtx":
            src = downDir / f
            dst = linkDir / (mat.name + ".mtx")
            print(f"{src} <- {dst}")
            try:
                os.symlink(src, dst)
            except FileExistsError:
                pass # dir already exists
            return

dataset = None
for ds in datasets.DATASETS:
    if ds.name == sys.argv[1]:
        dataset = ds
        break
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


# blacklist:
# cavity(\d+)_[bx].mtx
# circuit(\d+)_[bx].mtx
# other things that end in _b.mtx?
#