import collections
import sys

import ssgetpy

from lib import dtypes

Dataset = collections.namedtuple("Dataset", ["name", "mats"])

def safe_dir_name(s):
    t = s.strip()
    t = t.replace(" ", "_")
    t = t.replace("/", "_")
    t = t.replace("-", "_")
    t = t.lower()
    return t

def mat_is_real(mat):
    val = dtypes.DTYPES[(mat.group, mat.name)] == "real"
    return val

def filter_keep_real(mats):
    return [mat for mat in mats if mat_is_real(mat)]

def mat_is_small(mat):
    return (mat.rows < 1_000 and mat.cols < 1_000) \
        or mat.nnz < 20_000

def mat_is_large(mat):
    return (mat.rows > 1_000_000 and mat.cols > 1_000_000) \
        or mat.nnz > 20_000_000

def filter_reject_large(mats):
    return [mat for mat in mats if not mat_is_large(mat)]

def filter_reject_small(mats):
    return [mat for mat in mats if not mat_is_small(mat)]

## all real-valued matrices
REAL_MATS = Dataset(
    name = "reals",
    mats = filter_keep_real(ssgetpy.search(
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

mats = []
for kind in kinds:
    mats += ssgetpy.search(
        kind=kind,
        dtype='real',
        limit=1_000_000
    )
REGULAR_REAL_MATS = Dataset(
    name="regular_reals",
    mats = filter_keep_real(mats)
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
    # REAL_MATS,
    REAL_SMALL_MATS,
    REAL_MED_MATS,
    # REGULAR_REAL_MATS,
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
    return kinds

for kind in get_kinds():
        d = Dataset(
            name = "kind_"+safe_dir_name(kind),
            mats = filter_reject_large( \
            filter_reject_small( \
            filter_keep_real(ssgetpy.search(
                kind=kind,
                dtype='real',
                limit=1_000_000
            ))))
        )
        if len(d.mats) > 0:
            DATASETS += [d]
