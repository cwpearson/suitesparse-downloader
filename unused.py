"""list unused data in suitesparse"""

import os
from pathlib import Path, PurePath
import sys

from lib import config
from lib import datasets

used = set()

for dataset in datasets.DATASETS:

    # check if dataset directory exists
    if not os.path.isdir(config.DIR / dataset.name):
        continue

    for f in os.listdir(config.DIR / dataset.name):
        if f.endswith(".mtx"):
            used.add(f[:-4])

for f in os.listdir(config.DIR / "suitesparse"):
    if f not in used:
        print(os.path.abspath(config.DIR / "suitesparse" / f))




