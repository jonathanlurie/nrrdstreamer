import sys
import os.path
import ntpath
import numpy as np
import nrrd
import time
import tools


def readnrrd(nrrd_path, position):
    data, header = nrrd.read(nrrd_path, index_order='F')
    return data[int(position[0]), int(position[1]), int(position[2])]


if __name__ == "__main__":
    # Parameters
    if len(sys.argv) < 3:
        print('Usage: python readnrrd.py /path/to/file.nrrd x,y,z')
        sys.exit(1)
    input_nrrd = sys.argv[-2]
    position = sys.argv[-1].split(',')
    start = time.time()
    val = readnrrd(input_nrrd, position)
    end = time.time()
    print('time:', (end - start))
    print(val)
