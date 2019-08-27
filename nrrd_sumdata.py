import sys
import os.path
import ntpath
import numpy as np
import nrrd
import time
import tools


if len(sys.argv) != 2:
    print("This script sums up all the values of the voxels and prints the sum.")
    print("args should be:")
    print("python nrrd_sumdata.py <input.nrrd>")
    exit()

input = sys.argv[-1]

data, header = nrrd.read(input)

sum = data.sum()
print(sum)
