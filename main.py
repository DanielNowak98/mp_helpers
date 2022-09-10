

import cv2
import mediapipe as mp
from mp_helpers import Mp_helpers
from webcam_helpers import Webcam
from image_helpers import Image

from pose_media import mediapipe_pose



cam = Webcam()
IMG = Image()
mp = Mp_helpers()


cap = cam.get_webcam_feed()

with mp.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():

    
        ret, frame = cam.get_frame()

        image, results = mp.mediapipe_detection(frame,holistic)

        mp.draw_styled_landmarks(image, results)
        mp.get_coordinates(results)

        cv2.imshow("Frame", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

        










