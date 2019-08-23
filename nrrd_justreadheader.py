import sys
import os.path
import ntpath
import numpy as np
import nrrd
import time
import tools

header = nrrd.read_header(sys.argv[-1])
# print(header)

header["space directions"] = header["space directions"].tolist()

space_directions_fixed = []
for col in header["space directions"]:
    if not np.isnan(col).any():
        space_directions_fixed.append(col)

print(space_directions_fixed)
