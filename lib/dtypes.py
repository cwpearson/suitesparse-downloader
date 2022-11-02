"""export a map that is (group, name) -> dtype for all mats"""

import requests
import datetime
import os

import scipy.io

from lib import config

def download_ss_index(path):

    path_dir = path.parent
    path_dir.mkdir(parents=True, exist_ok=True) 

    with open(path, "wb") as f:
        req = requests.get(config.SS_ROOT_URL + "/files/ss_index.mat")
        f.write(req.content)

def ensure_ss_index(path):
    if not os.path.exists(path):
        download_ss_index(path)
    mtime = datetime.datetime.utcfromtimestamp(os.path.getmtime(config.DIR / ".ss_index.mat"))
    if datetime.datetime.utcnow() - mtime > datetime.timedelta(days=90):
        download_ss_index(path)

# download metadata file if missing
local = config.DIR / ".ss_index.mat"
ensure_ss_index(local)


# load metadata and convert to a database
mat = scipy.io.loadmat(config.DIR / ".ss_index.mat", squeeze_me=True)

s = mat["ss_index"].item()
# for i,x in enumerate(s):
#     print(i, x)
groups = s[1]
names = s[2]
# 3 letters, first letter:
# r=real, p=binary, c=complex, i=integer
rbtype = s[19] 

def dtype_from_rbtype(rbtype):
    if rbtype[0] == "r":
        return "real"
    elif rbtype[0] == "p":
        return "binary"
    elif rbtype[0] == "c":
        return "complex"
    elif rbtype[0] == "i":
        return "integer"
    else:
        raise LookupError

DTYPES = {}
for i in range(len(names)):
    DTYPES[(groups[i], names[i])] = dtype_from_rbtype(rbtype[i])
