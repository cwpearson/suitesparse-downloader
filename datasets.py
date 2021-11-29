import collections
import sys

import ssgetpy

import lists

Dataset = collections.namedtuple("Dataset", ["name", "mats"])

def safe_dir_name(s):
    t = s.strip()
    t = t.replace(" ", "_")
    t = t.replace("/", "_")
    t = t.replace("-", "_")
    t = t.lower()
    return t

def filter_reject_blacklist(mats):
    filtered = []
    for mat in mats:
        if mat.name in lists.INTEGER_MATS:
            print(f"BLACKLIST {mat.name}")
            continue
        filtered += [mat]
    return filtered

def filter_reject_large(mats):
    filtered = []
    for mat in mats:
        if mat.rows > 1_000_000 or mat.cols > 1_000_000 or mat.nnz > 20_000_000:
            continue
        filtered += [mat]
    return filtered

def filter_reject_small(mats):
    filtered = []
    for mat in mats:
        if mat.rows < 1_000 or mat.cols < 1_000 or mat.nnz < 20_000:
            continue
        filtered += [mat]
    return filtered

## all real-valued matrices
REAL_MATS = Dataset(
    name = "reals",
    mats = filter_reject_blacklist(ssgetpy.search(
        dtype='real',
        limit=1_000_000
    ))
)

## certain matrices with regular structure 
kinds = [
    "2D/3D",
    "Acoustics Problem",
    "Materials Problem",
    "Structural Problem",
    "Computational Fluid Dynamics Problem",
    "Model Reduction Problem",
    "Semiconductor Device Problem",
    "Theoretical/Quantum Chemistry Problem",
    "Thermal Problem",
]
REGULAR_REAL_MATS = Dataset(
    name = "regular_reals",
    mats = []
)
mats = []
for kind in kinds:
    mats += ssgetpy.search(
        kind=kind,
        dtype='real',
        limit=1_000_000
    )
REGULAR_REAL_MATS = Dataset(
    name="regular_reals",
    mats = filter_reject_blacklist(mats)
)

## keep "small" matrices
REGULAR_REAL_SMALL_MATS = Dataset (
    name = "regular_reals_small",
    mats = filter_reject_large(REGULAR_REAL_MATS.mats)
)
REAL_SMALL_MATS = Dataset (
    name = "reals_small",
    mats = filter_reject_large(REAL_MATS.mats)
)

## keep "medium" matrices
REGULAR_REAL_MED_MATS = Dataset (
    name = "regular_reals_med",
    mats = filter_reject_large(filter_reject_small(REGULAR_REAL_MATS.mats))
)
REAL_MED_MATS = Dataset (
    name = "reals_med",
    mats = filter_reject_large(filter_reject_small(REAL_MATS.mats))
)







## export all datasets
DATASETS  = [
    REAL_MATS,
    REAL_SMALL_MATS,
    REAL_MED_MATS,
    REGULAR_REAL_MATS,
    REGULAR_REAL_SMALL_MATS,
    REGULAR_REAL_MED_MATS
]

def get_kinds():
    """return set of unique kind fields"""

    mats = ssgetpy.search(
        limit=1_000_000
    )

    kinds = set()
    for mat in mats:
        kinds.add(mat.kind)
    print(f"kinds: {kinds}")

    return kinds

for kind in get_kinds():
        d = Dataset(
            name = "kind_"+safe_dir_name(kind),
            mats = filter_reject_blacklist(ssgetpy.search(
                kind=kind,
                dtype='real',
                limit=1_000_000
            ))
        )
        if len(d.mats) > 0:
            DATASETS += [d]
