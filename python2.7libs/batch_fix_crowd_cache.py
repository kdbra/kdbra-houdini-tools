import argparse
from os import path, listdir



parser = argparse.ArgumentParser(description='Batch fix crowd cache')
parser.add_argument('input_dir',type=str,
                    help='sequence directory')
parser.add_argument('wrong_path',type=str,
                    help='search in *.geo for this path')
parser.add_argument('new_path',type=str,
                    help='replace found path with this')

args = parser.parse_args()

input_dir = args.input_dir
search_path = args.wrong_path
new_path = args.new_path
listd = listdir(input_dir)

for item in listd:
    item_path = path.join(input_dir, item)
    if path.isfile(item_path):
        tmp = ""
        with open(item_path, "r") as file:
            for line in file:
                tmp += line.replace(search_path,new_path)
        file = open(item_path, "w")
        file.write(tmp)
        file.close()
    print "{} fixed".format(item)

#print("{}\n{}\n{}\n{}".format(input_dir, search_path, new_path,listd))