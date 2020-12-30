# 修改自voc_annotation.py
# 用于训练，标注文件路径和box信息

import xml.etree.ElementTree as ET
from os import getcwd
import os

sets=['train', 'val', 'test']

classes = ["fire"]

# def convert_annotation(image_id, list_file):
#     in_file = open('dataset/train/images/%s.txt'%(image_id))
    

wd = getcwd()
# train
image_set = 'train'
image_ids = open('dataset/main/%s.txt'%(image_set)).read().strip().split()
list_file = open('traindata.txt', 'w')
print(len(image_ids))
for image_id in image_ids:
    with open('dataset/train/annotations/%s.txt'%(image_id)) as f:
        ls = f.readlines()
        for l in ls:
            s = l.strip().split(' ')
            s[0] = wd + '/dataset/train/images/' + s[0]
            s[1] = ' '
            s[2] = s[2] + ','
            s[3] = s[3] + ','
            s[4] = s[4] + ','
            s[5] = s[5] + ','
            s.append('0\n')
            for _ in s:
                list_file.write(_)
                
        
    # convert_annotation(image_id, list_file)
    # list_file.write('\n')
list_file.close()

# # val
# image_set = 'val'
# image_ids = open('dataset/main/%s.txt'%(image_set)).read().strip().split()
# list_file = open('%s.txt'%(image_set), 'w')
# for image_id in image_ids:
#     list_file.write('%s/dataset/train/images/%s.jpg'%(wd, image_id))
#     convert_annotation(image_id, list_file)
#     list_file.write('\n')
# list_file.close()

# #test
# image_set = 'test'
# image_ids = open('dataset/main/%s.txt'%(image_set)).read().strip().split()
# list_file = open('%s.txt'%(image_set), 'w')
# for image_id in image_ids:
#     list_file.write('%s/dataset/test/images/%s.jpg'%(wd, image_id)) # 目录区别 Fires/test
#     convert_annotation(image_id, list_file)
#     list_file.write('\n')
# list_file.close()



# for image_set in sets:
#     image_ids = open('Fires/main/%s.txt'%(image_set)).read().strip().split()
#     list_file = open('%s.txt'%(image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/Fires/train/images/%s.jpg'%(wd, image_id))
#         convert_annotation(image_id, list_file)
#         list_file.write('\n')
#     list_file.close()


