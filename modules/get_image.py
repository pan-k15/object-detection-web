from PIL import Image
import os

class GetImage:
    def __init__(self, img_file=""):
        self.img_path = img_file
        
    def get_dir(self):
        exp_dirs = []
        for filename in os.listdir(self.img_path):
            f = os.path.join(self.img_path, filename)
            # checking if it is a directory
            if os.path.isdir(f):                    
                exp_dirs.append(f)
                
        #print(exp_dirs)
        
        return exp_dirs
    
