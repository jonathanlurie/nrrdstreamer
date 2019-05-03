import sys
import os.path
import ntpath
import numpy as np
import nrrd
import tools


def readnrrd(nrrd_path, position):
    data, header = nrrd.read(nrrd_path, index_order='F')
    data_flat = data.flatten(order='F')

    xsize = header['sizes'][0]
    ysize = header['sizes'][1]
    zsize = header['sizes'][2]

    x = int(position[0])
    y = int(position[1])
    z = int(position[2])

    index_flat = xsize * ysize * z + xsize * y + x
    return data_flat[index_flat]


if __name__ == "__main__":
    # Parameters
    if len(sys.argv) < 3:
        print('Usage: python readnrrd.py /path/to/file.nrrd x,y,z')
        sys.exit(1)
    input_nrrd = sys.argv[-2]
    position = sys.argv[-1].split(',')
    val = readnrrd(input_nrrd, position)
    print(val)
