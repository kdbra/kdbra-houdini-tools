import glob
from os import path, listdir

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