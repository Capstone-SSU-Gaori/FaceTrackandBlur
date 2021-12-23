import pandas as pd
import cv2
from face_tracker_dlib import start_tracker,get_all_crops,get_all_lists    # dlib으로 detection: face_tracker_dlib으로, MTCNN으로 detection: face_tracker로

start_tracker('short.mp4') # 여기에 처리할 영상 이름 및 경로 입력 
positions_with_obj_id_frame_id_list=get_all_lists()
crop_img_with_obj_id_list=get_all_crops()

# df=pd.DataFrame(positions_with_obj_id_frame_id_list)
# df.to_csv("좌표들.csv",header=None,index=None)

# for i,c in enumerate(crop_img_with_obj_id_list):
#     cv2.imwrite(str(c[0])+".png",c[1])   -> 이렇게 하면 id.png 로 대표 얼굴 저장됨니다