



import os, shutil
folder = '.'
image_file = os.listdir(folder)

B = []
for i in image_file:
        file = i.split('.')[0]
        print(file)
        B.append(file)

print(B)
