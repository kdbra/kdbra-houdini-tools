#!/usr/bin/env python3
import argparse, subprocess, glob, os.path

parser = argparse.ArgumentParser(description='Batch convert Houdini geometry')
parser.add_argument('input_dir', type=str, help='directory')
parser.add_argument('-i', '--input_format', type=str, help='input format', default="geo")
parser.add_argument('-o', '--output_format', type=str, help='output format', default="bgeo.sc")

args = parser.parse_args()
items = glob.glob(os.path.join(args.input_dir, "*." + args.input_format))

for item in items:
	path, filename = os.path.split(item)
	name, ext = os.path.splitext(filename)
	new_path = os.path.join(path, '%s.%s' % (name, args.output_format))
	subprocess.call(["gconvert", item, new_path])
	print "{} converted to {}".format(item, args.output_format)