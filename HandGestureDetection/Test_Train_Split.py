import os
import random
import shutil

path_f = "Dataset/Training/TwoFinger"
path_t = "Dataset/Testing/TwoFinger"

print("Before " + str(len(os.listdir(path_f))))

print(str(len(os.listdir(path_t))))

#randomly moving 100 images for validation dataset
for i in range(100):
    file = random.choice(os.listdir(path_f))
    shutil.move(path_f +"/"+ file, path_t)

print("After " + str(len(os.listdir(path_f))))

print(str(len(os.listdir(path_t))))