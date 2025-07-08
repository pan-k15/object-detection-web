from charset_normalizer import detect
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from modules.load_model import Detect
from modules.get_image import GetImage
import time
#from Modules.ocr_module import Read_text
#from Modules.date_module import Clean_Date
from datetime import date
import cv2
import os
import shutil

today = date.today()
#file_name = 'data_' + str(today)+'.csv'
st.title('Upload Images')
# Include PIL, load_image before main()

values = st.slider(
    "Select a confidence",
    0.0, 1.0,0.4)
st.write("Values:", values)




def load_image(image_file):
	img = Image.open(image_file)
	newsize = (640, 640)
	im1 = img.resize(newsize)
	return im1


def read_img(model,img):
	detect = Detect(model_path=model, yolo='yolov5m',conf=values)
	res = detect.run(img)
	return res


st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"],accept_multiple_files=True)







if st.button("Reset", type="primary"): 
 
	# Parent Directory

	# Path
	path = "runs"
	
	# Remove the Directory
	# "Geeks"
	shutil.rmtree(path)
 
else:
    if image_file is not None:
        st.header('Results')
        result = []
        for img_file in image_file:
            img = load_image(img_file)
            st.image(img,width=200)
            res = read_img(model=None, img=img)

            st.dataframe(res)
            
            st.divider()
            
        isExist = os.path.exists("./runs/detect/")
        if isExist:
            st.header('Detection')
            get_img = GetImage(img_file="./runs/detect/")
            im_dir = get_img.get_dir()
        
        
            for detect in im_dir:
                for filename in os.listdir(detect):
                    f = os.path.join(detect, filename)
                    if os.path.isfile(f):
                        img2 = load_image(f)
                        st.image(img2,width=350)
				
			