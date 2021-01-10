#!/usr/bin/env python2.7
import os

hfs = os.environ["HFS"]
with  os.popen("hconfig -ap") as f:
	houdini_path = [l for l in f.readlines() if "HOUDINI_PATH :=" in l][0].split(":")
houdini_path = [p for p in houdini_path if os.path.exists(p) and hfs not in p]

print "{}".format(houdini_path)