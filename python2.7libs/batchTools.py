import glob, hou, datetime
from os import path, listdir, environ

def fixCrowdCache(input_dir, search_path,new_path):
    list_geos = glob.glob(path.join(input_dir, "*.geo"))
    for item in list_geos:
        tmp = ""
        with open(item, "r") as file:
            for line in file:
                tmp += line.replace(search_path,new_path)
        file = open(item, "w")
        file.write(tmp)
        file.close()
        print "{} fixed".format(item)

default_render_path = path.join(environ["HIP"], "render/*")
def checkRenderTime(path_to_folder=default_render_path):
    files = glob.glob(path_to_folder)
    mtimes = []
    for file in files:
        mt = path.getmtime(file)
        mtimes.append(mt)
    mtimes.sort()
    delta = mtimes[-1] - mtimes[0]
    return str(datetime.timedelta(seconds=delta))