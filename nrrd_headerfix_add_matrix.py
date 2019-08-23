import sys
import os.path
import ntpath
import numpy as np
import nrrd
import time
import tools


if len(sys.argv) != 4:
    print("This script adds the 'space direction' matrix. It will be a diagonal matrix with the resolution")
    print("args should be:")
    print("<input.nrrd> <output.nrrd> <resolution>")
    exit()

input = sys.argv[-3]
output = sys.argv[-2]
res = float(sys.argv[-1])


data, header = nrrd.read(input)

matrix = [[res, 0, 0], [0, res, 0], [0, 0, res]]
if header["dimension"] == 4:
    matrix.insert(0, None)

header["space directions"] = matrix
header["space dimension"] = 3
nrrd.write(output, data, header=header)
