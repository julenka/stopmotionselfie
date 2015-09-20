#!/usr/bin/env python
# coding=utf-8
""" Combines pictures from a given output directory into a video

Example:
python make_video.py --out test.avi --framerate 10 jpegs/20150919

"""
__author__ = 'julenka'
import argparse
import sys
import subprocess
import os

def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", "-o", default="out.avi", help="output filename")
    parser.add_argument("--framerate", "-r", type=int, default=10, help="output video framerate")
    parser.add_argument("dir", help="directory containing input pictures")
    return parser.parse_args(argv)


def make_video(out, pictures_dir, video_framerate):
    command = "ffmpeg -pattern_type glob -r {} -i '{}' {}".format(
        video_framerate,
        os.path.join(pictures_dir, "*.jpeg"),
        out
    )
    print(command)
    subprocess.call(command, shell=True)

def main():
    args = parse_args(sys.argv[1:])
    make_video(args.out, args.dir, args.framerate)

if __name__ == '__main__':
    main()