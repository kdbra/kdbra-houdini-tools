import glob, hou, datetime
import os.path
from os import environ

def fixCrowdCache(input_dir, search_path,new_path):
    list_geos = glob.glob(os.path.join(input_dir, "*.geo"))
    for item in list_geos:
        tmp = ""
        with open(item, "r") as file:
            for line in file:
                tmp += line.replace(search_path,new_path)
        file = open(item, "w")
        file.write(tmp)
        file.close()
        print "{} fixed".format(item)


def checkRenderTime(path="HIP", pattern="*"):
    if not os.path.exists(path):
        path = environ[path]
    path_to_folder = os.path.join(path, pattern)
     
    files = glob.glob(path_to_folder)
    mtimes = []
    for file in files:
        mt = os.path.getmtime(file)
        mtimes.append(mt)
    mtimes.sort()
    delta = mtimes[-1] - mtimes[0]
    return str(datetime.timedelta(seconds=delta))