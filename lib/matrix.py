class Matrix:
    def __init__(self, group, name, dtype, nrows, ncols, nnz):
        self.group = group
        self.name = name
        self.dtype = dtype
        self.nrows = int(nrows)
        self.ncols = int(ncols)
        self.nnz = int(nnz)

    def to_tuple(self):
        return (self.group, self.name, self.dtype, self.nrows, self.ncols, self.nnz)

    def __repr__(self):
        return repr(self.to_tuple())

    def url(self):
        return "/".join(("https://sparse.tamu.edu", "MM", self.group, self.name + ".tar.gz"))