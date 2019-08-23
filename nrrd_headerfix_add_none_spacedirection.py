import sys
import os.path
import ntpath
import numpy as np
import nrrd
import time
import tools


if len(sys.argv) != 4:
    print("This script fixes the 'space direction' by adding a 'none' at the begining (component) or at the end (time). It also fixes the 'domains' accordingly.")
    print("args should be:")
    print("<input.nrrd> <output.nrrd> <component|time>")
    exit()

input = sys.argv[-3]
output = sys.argv[-2]
dim_type = sys.argv[-1]

if dim_type != "component" and dim_type != "time":
    print("The last argument must be 'component' or 'time'")
    exit()


data, header = nrrd.read(input)

if len(header["space directions"]) == header["dimension"]:
    print("No need to add none as a space direction, it already contains the right number of items.")
    exit()

modified = False

# so that we can add a None inside (not possible with np.ndarray)
header["space directions"] = header["space directions"].tolist()

if dim_type == "component":
    modified = True
    header["space directions"].insert(0, None)
    if "kinds" in header:
        header["kinds"].insert(0, "vector")

if dim_type == "time":
    modified = True
    header["space directions"].append(None)
    if "kinds" in header:
        header["kinds"].append("time")

if not modified:
    exit()

nrrd.write(output, data, header=header)
