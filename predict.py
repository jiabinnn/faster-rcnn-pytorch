#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from frcnn import FRCNN
from PIL import Image

frcnn = FRCNN()



# img = 'dataset/test/images/006486001008661.jpg'
# image = Image.open(img)

# r_image = frcnn.detect_image(image)
# r_image.save('result.jpg')

testdata_file = 'dataset/main/test.txt'
f = open(testdata_file)
lines = f.readlines()
result = open('result.txt', 'w')
for l in lines:
    l = l.strip()
    img = "dataset/test/images/%s.jpg"%l
    image = Image.open(img)    
    bbox, conf, label = frcnn.detect_image(image)
    

    if len(bbox)==0:
        continue
    
    for i in range(len(bbox)):
        score = conf[i] # 置信度
        left, top, right, bottom = bbox[i] # 框框位置
        result.write(l)
        result.write(' ' + str(score))
        result.write(' ' + str(left))
        result.write(' ' + str(top))
        result.write(' ' + str(right))
        result.write(' ' + str(bottom) + '\n')

result.close()

    
