import cv2
import numpy as np
import argparse
import os

def cropByColor(image, color):
    forward_index = np.where(image != color)

    right = max(forward_index[0])
    left = min(forward_index[0])
    bottom = max(forward_index[1])
    top = min(forward_index[1])

    return image[left:right, top:bottom]

def main():
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("imagePath")
    parser.add_argument("--backColor", default="white", type=str)
    args = parser.parse_args()

    # file information
    save_dir = os.path.dirname(args.imagePath)
    file_name = os.path.basename(args.imagePath)
    name, file_extension = os.path.splitext(file_name)

    # color set
    if args.backColor == "white":
        color = [255, 255, 255]
    if args.backColor == "black":
        color = [0, 0, 0]

    image = cv2.imread(args.imagePath)

    croped_image = cropByColor(image, [255, 255, 255])

    # save setting
    save_name = name + "-crop" + file_extension
    save_path = os.path.join(save_dir, save_name)
    cv2.imwrite(save_path, croped_image)

if __name__ == main:
    main()

