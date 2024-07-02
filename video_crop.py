import os,  glob, copy

import cv2
from tqdm import tqdm

videoFilenamesList = glob.glob('./videos//*.mp4', recursive=True)
for fname in tqdm(videoFilenamesList, total=len(videoFilenamesList)):

    # Capture video from the webcam
    cap = cv2.VideoCapture(fname)
    if cap.isOpened() == False:
        print("Can not open video %s"%(fname))
        continue
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
    fps = cap.get(cv2.CAP_PROP_FPS)  # 取得影像高度
    # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')          # 設定影片的格式為 MJPG
    fourcc = cv2.VideoWriter_fourcc('h', '2', '6', '4')

    # remove watermark
    # height = height - 20

    vid = cv2.VideoWriter(os.path.join('./artifacts', os.path.basename(fname).split('.')[0]+'_crop.mp4'), fourcc, fps, (width,  height-80))  # 產生空的影片

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            break

        img_save = copy.deepcopy(frame)
        img_save = img_save[80:height, :, :]
        
        vid.write(img_save)
    # Release the video capture and close the display window
    cap.release()
    vid.release()
    cv2.destroyAllWindows()