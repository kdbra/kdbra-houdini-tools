#!/usr/bin/env python
import os, argparse

parser = argparse.ArgumentParser(description='Setup shots directories')
parser.add_argument('-s', "--src", type=str, help='src directory', default="./src")
parser.add_argument('-n', '--scene_name', type=str, help='scene name', default="")
args = parser.parse_args()

def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

pwd = os.environ["PWD"]
shots = os.path.join(pwd, "shots")
mkdir(shots)


srcdir = os.path.abspath(args.src)
shotslist = os.listdir(srcdir)
scene = os.path.join(shots, args.scene_name)
mkdir(scene)

for shotname in shotslist:
    shotdir = os.path.join(scene, shotname)
    if os.path.isdir(os.path.join(srcdir, shotname)):
        print "{} directory created".format(shotdir)
        if not os.path.isdir(shotdir):
            os.mkdir(shotdir)
            hip = os.path.join(shotdir, "hip")
            trk = os.path.join(shotdir, "trk")
            nk = os.path.join(shotdir, "nk")
            dailies = os.path.join(shotdir, "dailies")
            proxy = os.path.join(shotdir, "proxy")
            mkdir(shotdir)
            mkdir(hip)
            mkdir(trk)
            mkdir(nk)
            mkdir(dailies)
            mkdir(proxy)
