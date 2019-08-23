#!/usr/bin/env python

"""
This script uncompresses a compressed NRRD file.
Encoding of the output will be 'raw' and the data blob will be inflated.
"""

import sys
import os.path
import numpy as np
import nrrd

if len(sys.argv) != 3:
    print("Incorrect arguments. Expected are:")
    print("nrrd_decompress.py <input nrrd> <output nrrd>")
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

data, header = nrrd.read(input_filename)
header["encoding"] = "raw"
nrrd.write(output_filename, data, header=header)
