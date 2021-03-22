#!/usr/bin/env python
import os, argparse

parser = argparse.ArgumentParser(description='Setup shots directories')
parser.add_argument('-s', "--src", type=str, help='src directory', default="./src")
parser.add_argument('-n', '--scene_name', type=str, help='scene name', default="")
args = parser.parse_args()

pwd = os.getcwd()

# get shot list 
shotslist = os.listdir(os.path.abspath(args.src))

for shotname in shotslist:
    paths = []
    # Note - you can make nested paths here    
    dirs = ['dailies',
             'hip',
             'trk',
             'trk/proxy',
             'one/two/three',
             'nk']
    for i in dirs:
        paths.append(os.path.join(pwd, 'shots', args.scene_name, shotname, i))

    for item in paths:
        if not os.path.exists(item):
            os.makedirs(item)