#!/usr/bin/env python2.7
import os

path = os.environ["PATH"]
hou_path = [ p for p in path.split(":") if "houdini" in p][0]
home = os.environ["HOME"]
print hou_path
print home