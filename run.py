import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("imagePath")

args = parser.parse_args()

image = cv2.imread(args.imagePath)

