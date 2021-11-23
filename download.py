import os
from pathlib import Path
import sys

import datasets

mats = datasets.ALL_REAL_MATS

print(len(mats))

scratchPath = Path(os.environ["SCRATCH"])
downPath = scratchPath / "suitesparse"
print("ensure", downPath)
try:
    os.makedirs(downPath)
except FileExistsError:
    pass # dir already exists

for mat in mats:

    print(mat.name)

    if os.path.exists(downPath / mat.name / (mat.name + ".mtx")):
        print(f"skipping {mat.name}: already exists")
        continue

    mat.download(format='MM', destpath=downPath, extract=True)

    # TODO: check download for a type that is not 'real' and remove if so

    # TODO: check for non-coordinate and remove, if so

    # many mats include rhs/whatever in extracted. toss that.
    files = os.listdir(downPath / mat.name)
    for f in files:
        if f != (mat.name + ".mtx"):
            print("DELETE ", f)
            os.remove(downPath / mat.name / f)

    files = os.listdir(downPath / mat.name)
    if len(files) == 0:
        os.rmdir(downPath / mat.name)


# blacklist:
# cavity(\d+)_[bx].mtx
# circuit(\d+)_[bx].mtx
# other things that end in _b.mtx?
#