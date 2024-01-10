import os
import shutil
from tqdm import tqdm

"""
删除目标文件夹下面的所有文件
"""
def delete_files_in_folder(target_folder):
    """删除目标文件夹下面所有的文件"""
    try:
        if os.path.exists(target_folder):
            for file in tqdm(os.listdir(target_folder)):
                file_path = os.path.join(target_folder,file)

                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Delete: {file}")

            print(f"All the files in {target_folder} have been deleted")

        else:
            print(f"The folder {target_folder} does not exist.")

    except Exception as e:
        print("failed to delete files, something went wrong")

if __name__ == "__main__":
    # 目标文件夹路径
    target_folder = r'F:\HITSZ_LearningMaterials\Python&PyTorch\unet-pytorch-main\ice_boll_data\VOC2007\JPEGImages'
    delete_files_in_folder(target_folder)