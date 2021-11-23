import datasets

for ds in datasets.DATASETS:
    print(f"{ds.name}: {len(ds.mats)} matrices")