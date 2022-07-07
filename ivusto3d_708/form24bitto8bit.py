#读取整个bacepath文件夹下的文件并且转换为8位保存到savepath
import os
import cv2
bacepath = "C:/patient3/"
savepath = 'C:/patient3_2/'

f_n  = os.listdir(bacepath)
print(f_n)
i=0
for n in f_n:
    imdir = bacepath + '\\' + n
    print(n)
    img = cv2.imread(imdir)
 
    cropped = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(savepath + '\\' + str(i)+'.jpg', cropped)#NOT CAHNGE THE TYPE
    i=i+1
