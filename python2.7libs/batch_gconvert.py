import argparse, subprocess, glob
from os import path, listdir
parser = argparse.ArgumentParser(description='Batch convert Houdini geometry')
parser.add_argument('input_dir',type=str, help='directory')
parser.add_argument('input_format',type=str, help='input format')
parser.add_argument('output_format',type=str, help='output format')

args = parser.parse_args()
directory = args.input_dir
informat = args.input_format
outformat = args.output_format
#listdir = listdir(directory)
items = glob.glob(path.join(directory, "*"+informat))

for item in items:
    item_path = path.join(directory, item)
    if path.isfile(item_path):
        name = path.splitext(item)[0]
        fmt = path.splitext(item)[1]
        if fmt == informat:
            new_path = path.join(directory, name + outformat)
            subprocess.run(["gconvert", item_path, new_path])
            print "{} converted to .bgeo.sc".format(item_path)