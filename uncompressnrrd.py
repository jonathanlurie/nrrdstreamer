import sys
import os.path
import ntpath
import numpy as np
import nrrd


if __name__ == "__main__":
    # Parameters
    if len(sys.argv) < 3:
        print('Usage: python readnrrd.py /path/to/input.nrrd /path/to/output.nrrd')
        sys.exit(1)
    input_nrrd = sys.argv[-2]
    output_nrrd = sys.argv[-1]

    # print(nrrd.write.__code__.co_varnames)
    # print(nrrd._version_)
    #
    data, header = nrrd.read(filename=input_nrrd)
    header["encoding"] = 'raw'
    nrrd.write(filename=output_nrrd, data=data, header=header)
