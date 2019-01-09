import cv2 as cv
from tqdm import tqdm
import numpy as np


# Step 3: To process all the frames


def bg_rm(im, im_bg):
    # Convert RGB color to gray color, in order to get "pure" white mask
    im_gray = cv.cvtColor(im, cv.COLOR_RGB2GRAY)

    # If the color of one pixel is very white (more than 210, from experience), mark it.
    im_mask = im_gray.copy()
    im_mask[im_mask < 210] = 0
    im_mask[im_mask > 210] = 255
    # To use median filter to remove noise.
    im_mask = cv.medianBlur(im_mask, 5)

    # To extend 1-layer mask to 3-layer mask.
    im_mask3 = np.zeros([1080, 1920, 3], np.uint8)
    im_mask3[:, :, 0] = im_mask
    im_mask3[:, :, 1] = im_mask
    im_mask3[:, :, 2] = im_mask

    # To remove the color of background.
    imo = np.int16(im) - np.int16(im_bg)

    # To add the mask of white part, in order to avoid white color becoming darker.
    imo = np.int16(imo) + np.int16(im_mask3)

    # To limit the range of uint 8.
    imo[imo > 255] = 255
    imo[imo < 0] = 0
    imo = np.uint8(imo)
    return imo


def main():
    # Background image loading
    im_bg = cv.imread('bg.bmp')

    # To process all the frames and output them.
    for i in tqdm(range(3762)):
        im = cv.imread('images/%04d.bmp' % i)
        imo = bg_rm(im, im_bg)
        cv.imwrite('out/%04d.bmp' % i, imo)


if __name__ == '__main__':
    main()
