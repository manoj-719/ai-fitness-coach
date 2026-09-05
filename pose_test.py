import cv2
import mediapipe as mp

mp_pose=mp.solutions.pose #give me mediapiipes pose functionality
mp_drawing=mp.solutions.drawing_utils #contains function s for drawing thngs such as points lines pose skeleton connections

cap=cv2.VideoCapture(0)#cap is connection to webvam
with mp_pose.Pose(           #we are mediapipe object
 static_image_mode=False,  #i am processing a video stream not independent photographs
 model_complexity=1,    #this controls the complexity of the pose model
 min_detection_confidence=0.5,
 min_tracking_confidence=0.5 #this is relatead to pose across frames
) as pose:   #stores the detecetor in the variable pose

        while cap.isOpened():
             ret,frame=cap.read()
             if not ret:
                  print("camera i snot detected")
                  break
             
          