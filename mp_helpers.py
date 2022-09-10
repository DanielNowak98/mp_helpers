import csv
import os
import numpy as np
import mediapipe as mp
import cv2


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

class Mp_helpers:

    def __init__(self):
        self.mp_drawing = mp_drawing
        self.mp_holistic = mp_holistic
        self.mp_pose = mp_pose
        self.mp_drawing_styles = mp_drawing_styles
        self.mp_face_mesh = mp_face_mesh
    
    
    def mediapipe_detection(self,image,model):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        image.flags.writeable = False                 
        results = model.process(image)                 
        image.flags.writeable = True                   
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
        return image, results
    
    def draw_styled_landmarks(self,image, results):
        # 1. Pose Connections

        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                                 self.mp_drawing.DrawingSpec(color=(112,112,112), thickness=1, circle_radius=1), 
                                 self.mp_drawing.DrawingSpec(color=(94,200,0), thickness=1, circle_radius=1)
                                 )

        # 2. Face Mesh
        self.mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
                                 mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                 )

        # 3. Right hand
        self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(80,22,10), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(80,44,121), thickness=1, circle_radius=1)
                                 )

        # 4. Left Hand
        self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                                 mp_drawing.DrawingSpec(color=(121,22,76), thickness=1, circle_radius=1),
                                 mp_drawing.DrawingSpec(color=(121,44,250), thickness=1, circle_radius=1)
                                 )
        
    def get_coordinates(self,results):

        pass

        index = ["WRIST","THUMB_CMC","THUM_MCP", "THUMB_IP", "THUMB_TIP", "INDEX_FINGER_MCP", 
        "INDEX_FINGER_PIP", "INDEX_FINGER_DIP", "INDEX_FINGER_TIP", "MIDDLE_FINGER_MCP","MIDDLE_FINGER_PIP",
         "MIDDLE_FINGER_DIP", "MIDDLE_FINGER_TIP", "RING_FINGER_PIP", "RING_FINGER_DIP", "RING_FINGER_TIP", 
         "PINKY_MCP", "PINKY_PIP", "PINKY_DIP", "PINKY_TIP"]



    
    
    

        




