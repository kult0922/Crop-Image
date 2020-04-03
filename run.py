import cv2
import numpy as np
import argparse
import os

def cropByAlpha(image):
    forward_index = np.where(image[:,:,3] != 0)

    right = max(forward_index[0])
    left = min(forward_index[0])
    bottom = max(forward_index[1])
    top = min(forward_index[1])

    return image[left:right, top:bottom]

def cropByColor(image, color):
    forward_index = np.where(image[:,:] != color)

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

    image = cv2.imread(args.imagePath, cv2.IMREAD_UNCHANGED)

    # color set
    if args.backColor == "white":
        color = [255, 255, 255]
    if args.backColor == "black":
        color = [0, 0, 0]

    # crop image
    print(image.shape)
    if image.shape[2] == 3:
        croped_image = cropByColor(image, color)
        print("color")
    elif image.shape[2] == 4:
        croped_image = cropByAlpha(image)
        print("alpha")

    # save setting
    save_name = name + "-crop" + file_extension
    save_path = os.path.join(save_dir, save_name)
    cv2.imwrite(save_path, croped_image)

if __name__ == "__main__":
    main()

