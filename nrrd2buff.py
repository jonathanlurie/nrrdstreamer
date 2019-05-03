import sys
import os.path
import ntpath
import numpy as np
import nrrd
import tools


def nrrd2buff(nrrd_path, output_folder):
    data, header = nrrd.read(nrrd_path, index_order='F')

    # converting the data to binary buffer
    data_flat = data.flatten(order='F')
    data_buffer = data_flat.tobytes()

    # converting the header to json
    header_nonumpy = {}
    for k, v in header.items():
        header_nonumpy[k] = v

        if(type(v) == np.ndarray):
            header_nonumpy[k] = v.tolist()

    # basename for output file
    filename_noext = ntpath.basename(nrrd_path).split('.')[0]

    # write the json header
    output_json = open(os.path.join(output_folder, filename_noext + '.json'), 'w')
    output_json.write(tools.to_json(header_nonumpy))
    output_json.close()

    # streams the file writing to not crash on larger files
    with open(os.path.join(output_folder, filename_noext + '.buf'), 'wb') as stream:
        total_len = len(data_buffer)
        chunk_size = 1024
        start = 0

        while(start < total_len):
            stream.write(data_buffer[start:start+chunk_size])
            start = start + chunk_size



if __name__ == "__main__":
    # Parameters
    if len(sys.argv) < 3:
        print('Usage: python nrrd2buff.py /path/to/file.nrrd /output/folder/')
        sys.exit(1)
    input_nrrd = sys.argv[-2]
    out_folder = sys.argv[-1]

    nrrd2buff(input_nrrd, out_folder)
