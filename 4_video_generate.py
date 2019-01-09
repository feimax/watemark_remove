import cv2 as cv
from tqdm import tqdm


# Step 4: To generate the video again.


def main():
    # To have a video writer and set frame-rate and resolution
    out = cv.VideoWriter('out.avi', 0, 30, (1920, 1080))
    # To write each frame to video.
    for i in tqdm(range(3762)):
        im = cv.imread('out/%04d.bmp' % i)
        out.write(im)
    out.release()


if __name__ == '__main__':
    main()
