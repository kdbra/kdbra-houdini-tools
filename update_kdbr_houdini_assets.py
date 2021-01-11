#!/usr/bin/env python2.7
import os
from sys import platform

kdbra = os.environ["KDBRA_HOUDINI_ASSETS"]
pwd = os.environ["PWD"]
search_names = ["otls", "hda", "toolbar"]
local_dirs = [ l for l in os.listdir(kdbra) if os.path.isdir(os.path.join(kdbra,l)) and any(n in l for n in search_names)]

mode = input("Type 'user' or 'TD' to choose sync direction:")
mode = 'user' if mode == '' else mode
print "You chosen {} mode".format(mode)

def update_repo_dirs(local_dirs, pwd):
	repo_dirs = [d for d in os.listdir(pwd) if os.path.isdir(os.path.join(pwd,d))]
	for ld in local_dirs:
		if ld in repo_dirs:
			print "directory /{} alredy exist".format(ld)
		else:
			new_path = os.path.join(pwd,ld)
			os.mkdir(new_path)
			print "directory {} created".format(new_path)

def compare_files(file0, file1):
	try:
		local_modified = os.stat(file0).st_mtime
		repo_modified = os.stat(file1).st_mtime
		if local_modified < repo_modified:
			print "repo is up to date"
		else:
			dest = os.path.split()[0]
			copy_file(file0, dest)
			print "{} copied to {}".format(file0, dest)
	except OSError:
		print "file does not exist"

def copy_file(file, dest_dir):
	if "linux" in platform:
		os.system("cp "+file+" "+dest_dir)
	elif "win" in platform:
		os.system("copy "+file+" "+dest_dir)

def compare_dirs(path0, path1):
	list0 = [f for f in os.listdir(path0) if os.path.isfile(os.path.join(path0,f))]
	list1 = [f for f in os.listdir(path1) if os.path.isfile(os.path.join(path1,f))]
	#print list0, "\n", list1
	for file0 in list0:

		if file0 in list1:
			print "{} alredy exists in {} ... checking for updates ...".format(file0, path1)
			compare_files(os.path.join(path0,file0),  os.path.join(path1,file0))

		else:
			print "{} does not exist in {} ... creating".format(file0, path1)
			copy_file(os.path.join(path0,file0),path1)


update_repo_dirs(local_dirs,pwd)

for local_dir in local_dirs:
	
	compare_dirs(os.path.join(kdbra, local_dir),os.path.join(pwd, local_dir))

