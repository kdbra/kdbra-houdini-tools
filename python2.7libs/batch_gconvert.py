#!/usr/bin/env python3
import argparse, subprocess, glob, os.path

parser = argparse.ArgumentParser(description='Batch convert Houdini geometry')
parser.add_argument('input_dir', type=str, help='directory')
parser.add_argument('input_format', type=str, help='input format')
parser.add_argument('output_format', type=str, help='output format')

args = parser.parse_args()
directory = args.input_dir
informat = args.input_format ? args.input_format : 'geo'
outformat = args.output_format ? args.output_format : 'bgeo.sc'

items = glob.glob(path.join(directory, "*." + informat))

for item in items:
	path, filename = os.path.split(item)
	name, ext = os.path.splitext(filename)

	new_path = os.path.join(path, '%s.%s' % (name, outformat))

	subprocess.call(["gconvert", item, new_path])
	print "{} converted to .bgeo.sc".format(item_path)