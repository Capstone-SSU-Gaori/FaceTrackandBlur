import pandas as pd
from face_tracker import start_tracker,get_all_crops,get_all_lists

start_tracker('short.mp4') # 여기에 처리할 영상 이름 및 경로 입력 
positions_with_obj_id_frame_id_list=get_all_lists()
crop_img_with_obj_id_list=get_all_crops()

# df=pd.DataFrame(test)
# df.to_csv("좌표들.csv",header=None,index=None)