import cv2
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("imagePath")
parser.add_argument("--backColor", type=str)
args = parser.parse_args()

save_dir = os.path.dirname(args.imagePath)
file_name = os.path.basename(args.imagePath)
name, file_extension = os.path.splitext(file_name)

image = cv2.imread(args.imagePath)

forward_index = np.where(image != [255, 255, 255])

right = max(forward_index[0])
left = min(forward_index[0])
bottom = max(forward_index[1])
top = min(forward_index[1])

#import pdb;pdb.set_trace()
croped_image = image[left:right, top:bottom]

save_name = name + "-crop" + file_extension
save_path = os.path.join(save_dir, save_name)

cv2.imwrite(save_path, croped_image)

