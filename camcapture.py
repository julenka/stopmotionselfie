#!/usr/local/bin/python
""" Capture pictures from webcamera to create stop motion video

Examples

Output to 'out' directory, capture every 60 seconds:
python camcapture.py

Output to 'mydir', capture every 30 seconds
python camcapture.py -o mydir -r 30

"""
import argparse
import cv2
import time
import datetime
import os
import sys
import time

def capture_frame(output_folder):	
    vidcap = cv2.VideoCapture()
    vidcap.open(0)
    time.sleep(3)
    retval, image = vidcap.retrieve()
    vidcap.release()
    file_name = os.path.join(output_folder, get_date_string() + ".jpeg")
    cv2.imwrite(file_name, image)
    print(file_name)

def get_date_string():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out-dir", "-o", default="out", help="output directory for images (default out)")
    parser.add_argument("--capture-rate", "-r", type=int, help="capture every X seconds (default 60)", default=60)
    return parser.parse_args(argv)

def main():
    args = parse_args(sys.argv[1:])
    out_dir = args.out_dir
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    while True:
        capture_frame(out_dir)
        time.sleep(args.capture_rate)

if __name__ == '__main__':
    main()