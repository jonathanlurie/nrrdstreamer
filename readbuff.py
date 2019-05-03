import sys
import os.path
import ntpath
import numpy as np
import nrrd
import json
import time
import tools

# corresponding types between nrrd file header field to numpy
NRRD_TYPES_TO_NUMPY = {
    "signed char": np.byte,
    "int8": np.int8,
    "int8_t": np.int8,
    "uchar": np.ubyte,
    "unsigned char": np.ubyte,
    "uint8": np.uint8,
    "uint8_t": np.uint8,
    "short": np.short,
    "short int": np.short,
    "signed short": np.short,
    "signed short int": np.short,
    "int16": np.int16,
    "int16_t": np.int16,
    "ushort": np.ushort,
    "unsigned short": np.ushort,
    "unsigned short int": np.ushort,
    "uint16": np.uint16,
    "uint16_t": np.uint16,
    "int": np.int32,
    "signed int": np.int32,
    "int32": np.int32,
    "int32_t": np.int32,
    "uint": np.uint32,
    "unsigned int": np.uint32,
    "uint32": np.uint32,
    "uint32_t": np.uint32,
    "longlong": np.int64,
    "long long": np.int64,
    "long long int": np.int64,
    "signed long long": np.int64,
    "signed long long int": np.int64,
    "int64": np.int64,
    "int64_t": np.int64,
    "ulonglong": np.uint64,
    "unsigned long long": np.uint64,
    "unsigned long long int": np.uint64,
    "uint64": np.uint64,
    "uint64_t": np.uint64,
    "float": np.float32,
    "double": np.float64
}


def readbuff(buf_path, headerjson_path, position):
    header = json.loads(open(headerjson_path, "r").read())

    nrrd_type = header['type']
    numpy_type = NRRD_TYPES_TO_NUMPY[nrrd_type]
    byte_size_per_voxel = np.dtype(numpy_type).itemsize


    xsize = header['sizes'][0]
    ysize = header['sizes'][1]
    zsize = header['sizes'][2]

    x = int(position[0])
    y = int(position[1])
    z = int(position[2])

    voxel_index_flat = xsize * ysize * z + xsize * y + x
    byte_index_flat = voxel_index_flat * byte_size_per_voxel

    stream = open(buf_path, "rb")
    stream.seek(byte_index_flat)
    byte_slice = stream.read(byte_size_per_voxel)
    stream.close()

    val = np.frombuffer(byte_slice, dtype=numpy_type)[0]
    return val


if __name__ == "__main__":
    # Parameters
    if len(sys.argv) < 3:
        print('Usage: python readnrrd.py /path/to/file.buf x,y,z')
        sys.exit(1)
    input_buf = sys.argv[-2]
    input_noext = input_buf[0: input_buf.rfind('.')]
    input_json = input_noext + '.json'
    position = sys.argv[-1].split(',')
    start = time.time()
    val = readbuff(input_buf, input_json, position)
    end = time.time()
    print('time:', 1000*(end - start), 'ms')
    print(val)
