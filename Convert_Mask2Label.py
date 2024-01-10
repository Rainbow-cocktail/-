"""
将label得到的掩码标签转化为用于训练的标签
"""

import os

import numpy as np
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt

Mask_path = r'./Mask'
Target_path = r'./SegmentationClass'

color_map = np.array([[0,0,0],[128,0,0],[0,128,0],[128,128,0]])
classes = ['_background_','1hole','hole','window']

# 画图
picture = True


if not os.path.exists(Target_path):
    os.makedirs(Target_path)

# 统计总体像素点类别数量，创建存储字典
pixel_statistics = {class_name: 0 for class_name in classes}

mask_list = os.listdir(Mask_path)
for mask in tqdm(mask_list):
    img = Image.open(os.path.join(Mask_path,mask))
    h,w = img.size # 获取图像高宽
    out_img = np.zeros(shape=(h,w))
    img = np.array(img) # (512, 512, 3)

    for i in range(len(color_map)):
        # 匹配语句直接用 ‘==’ 号判断即可
        temp = img == color_map[i]

        # 判断是否为彩色图像
        if len(img.shape) > 2:
            temp = temp.all(-1) # 沿着通道维压缩, 三个全true才为true
        out_img[temp] = i

        # 统计某张图片下，第i个颜色出现次数，并统计到总体字典里面
        pixel_statistics[classes[i]] += np.sum(temp)


    out_img = Image.fromarray(np.array(out_img,np.uint8)) # 图像数据为 0~255 int
    out_img.save(os.path.join(Target_path,mask))

# 输出统计结果
print('-' * 55)
print("| %15s | %15s | %15s |"%("class","class_num","pixels count"))
print('-' * 55)
for i , (class_name, num) in enumerate(pixel_statistics.items()):
    print("| %15s | %15s | %15s |"%(class_name,i,str(num)))
    print('-' * 55)


# 绘制像素值统计图
if picture is True:
    plt.pie(pixel_statistics.values(), labels=pixel_statistics.keys(), autopct='%1.1f%%', startangle=90)
    plt.title('Pixel Distribution for Each Class')
    plt.legend(title='Classes')
    plt.show()












