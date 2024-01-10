"""
获取图片中，不同颜色对应的RGB数值，并进行展示
image_path 可以接受单张图片路径(推荐) 也可以接受图片文件夹路径
在接受图片文件夹路径时，需要输入文件夹底下图片通道数
"""

from PIL import Image
import numpy as np
import os
from tqdm import tqdm

def count_unique_colors(image_path,c=None):
    if not os.path.exists(image_path):
        return print("targeted images not exist")


    if os.path.isfile(image_path):
        """对单张图片操作"""
        img = np.array(Image.open(image_path))  # (H,W,C)

        if c == 1:
            h,w = img.shape[0],img.shape[1]
            img = img.reshape(h,w,1)

        # 合并高和宽 每一行表示一个像素的 RGB 值 (HxW,C)
        unique_colors = np.unique(img.reshape(-1, img.shape[2]), axis=0)
        return unique_colors
    elif os.path.isdir(image_path):
        """对一个文件夹下面图片进行操作"""
        img_list = os.listdir(image_path)
        c = int(input("你真正对一个文件夹图片进行操作,请输入待处理图像通道数: "))
        combined = np.zeros(shape=(1,c))
        for each in tqdm(img_list):
            path = os.path.join(image_path,each)

            # 进行迭代
            single = count_unique_colors(path,c)

            # 将以往的和现在获取到的颜色表concat，再根据行去重
            combined = np.unique(np.concatenate((combined,single)),axis=0)
        return combined
    else:
        print('something went wrong')


if __name__ == "__main__":
    # 修改这个路径即可
    img_path = r'F:\HITSZ_LearningMaterials\Python&PyTorch\unet-pytorch-main\segmentation-format-fix-main\segmentation-format-fix-main\SegmentationClass'
    unique_colors = count_unique_colors(img_path)



    # 打印相关信息
    print(f"Total unique colors: {len(unique_colors)}")
    if len(unique_colors[0]) == 3:
        """对mask-RGB图像进行颜色种类查看"""
        for color in unique_colors:
            if np.sum(color != 0):
                print(f'RGB:{color}')
            else:
                print(f"RGB: {color} black background")
    if len(unique_colors[0]) == 1:
        """对标签进行查看"""
        for i in unique_colors:
            if i == 0:
                print(f'{i} : backgound')
            else:
                print(f'{i} : class {i}')