import cv2 as cv
from tqdm import tqdm


# Step 2: To obtain all the frames and saved as bmp format picture(lossless format).


def main():
    video_file_name = 'video.mp4'
    cap = cv.VideoCapture(video_file_name)

    total_frame = cap.get(cv.CAP_PROP_FRAME_COUNT)
    print('Total:', total_frame)
    print('Width:', cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print('Height:', cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print('FPS:', cap.get(cv.CAP_PROP_FPS))

    for i in tqdm(range(int(total_frame))):
        ret, frame = cap.read()
        cv.imwrite('images/%04d.bmp' % i, frame)


if __name__ == '__main__':
    main()
