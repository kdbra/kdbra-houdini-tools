#!/usr/bin/env python3
import argparse, subprocess, glob, os.path

parser = argparse.ArgumentParser(description='Batch render .rs')
parser.add_argument('-i', '--input', type=str, help='input pattern', default="./*.rs")

args = parser.parse_args()
items = glob.glob(args.input)
items.sort()
for item in items:
    print(item)
for item in items:
    subprocess.call(["/usr/redshift/bin/redshiftCmdLine", item])
    print("{} rendered".format(item))