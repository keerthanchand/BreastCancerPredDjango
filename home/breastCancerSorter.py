



import os, shutil
folder = './media/images'
image_file = os.listdir(folder)

for i in image_file:
        print(i.split('.')[0])
