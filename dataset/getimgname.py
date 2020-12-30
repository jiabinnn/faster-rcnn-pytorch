# 从VOCdevkit/VOC2007/voc2frcnn.py修改过来
# 把数据集文件名保存起来

import os
import random 
# copy of voc2frcnn
txtfilepath_trainval=r'./dataset/train/annotations'
txtfilepath_test=r'./dataset/test/images'

saveBasePath=r"./dataset/main/"
 
trainval_percent=1
train_percent=1

temp_txt = os.listdir(txtfilepath_trainval)
total_txt = []
for txt in temp_txt:
    if txt.endswith(".txt"):
        total_txt.append(txt)

num=len(total_txt)  
list=range(num)  
tv=int(num*trainval_percent)  
tr=int(tv*train_percent)  
trainval= random.sample(list,tv)  
train=random.sample(trainval,tr)  
 
print("train and val size",tv)
print("train size",tr)
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')  
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')  
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')  
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')  
 
for i  in list:  
    name=total_txt[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
# -----------------
# 添加test文件夹里的文件名
temp = os.listdir(txtfilepath_test)
total = []
for jpg in temp:
    if jpg.endswith(".jpg"):
        total.append(jpg)

num=len(total)  
list=range(num)
for i  in list:  
    name=total[i][:-4]+'\n'     
    ftest.write(name)  
print("test size ",num)

# -----------------
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
