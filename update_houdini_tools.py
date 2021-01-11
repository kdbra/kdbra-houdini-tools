#!/usr/bin/env python2.7
import os
from sys import platform

kdbra = os.environ["KDBRA_HOUDINI_ASSETS"]
pwd = os.environ["PWD"]
search_names = ["otls", "hda", "toolbar"]
local_dirs = [ l for l in os.listdir(kdbra) if os.path.isdir(os.path.join(kdbra,l)) and any(n in l for n in search_names)]

def update_repo_dirs(local_dirs, pwd):
	repo_dirs = [d for d in os.listdir(pwd) if os.path.isdir(os.path.join(pwd,d))]
	for ld in local_dirs:
		if ld in repo_dirs:
			print "directory /{} alredy exist".format(ld)
		else:
			new_path = os.path.join(pwd,ld)
			os.mkdir(new_path)
			print "directory {} created".format(new_path)

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def compare_files(file0, file1):
	try:
		local_modified = os.stat(file0).st_mtime
		repo_modified = os.stat(file1).st_mtime
		if local_modified < repo_modified:
			r = False
		else:
			r = True
		return r

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
	dirname = os.path.split(path0)[-1]
	files_to_copy = {dirname:[]}
	for file0 in list0:

		if file0 in list1:
			print "{} alredy exists in {} ... checking for updates ...".format(file0, path1)
			if compare_files(os.path.join(path0,file0),  os.path.join(path1,file0)):
				files_to_copy[dirname].append(file0)

		else:
			files_to_copy[dirname].append(file0)
	return files_to_copy
	
def clean_str(string):
	for char in '()[]} {?.!/;:':  
		string = string.replace(char,'')
	return string

update_repo_dirs(local_dirs,pwd)

files_to_copy = {}
for local_dir in local_dirs:
	files_to_copy = merge_two_dicts(files_to_copy, compare_dirs(os.path.join(kdbra, local_dir),os.path.join(pwd, local_dir)))

#print files_to_copy

numbered_list = []
list_to_copy = []
c = 0
for d in files_to_copy.keys():
	numbered_list.append(d)
	for i, f in enumerate(files_to_copy[d]):
		numbered_list.append(" ".join((str(c),f)))
		list_to_copy.append(f)
		c += 1

tmp_list = "\n".join(numbered_list)
#print tmp_list
#print list_to_copy
print "These files are to be copied from '{}' to '{}':\n{}".format(kdbra,pwd,tmp_list)
resp = clean_str(str(input("Select files to copy (python list slice syntax)")))
#print resp
list_to_copy = list_to_copy[int(resp[0]):int(resp[0])+1 if len(resp)<=1 else int(resp[1])]
print list_to_copy
