#8:2划分
import os
import random
import shutil
import nibabel as nib

# 输入文件夹路径
blur_folder = "LPBlur/blur"
sharp_folder = "LPBlur/sharp"

# 输出文件夹路径
train_blur_folder = "LPBlur/train/blur"
train_sharp_folder = "LPBlur/train/sharp"
val_blur_folder = "LPBlur/test/blur"
val_sharp_folder = "LPBlur/test/sharp"

# 创建输出文件夹
if not os.path.exists(train_blur_folder):
    os.makedirs(train_blur_folder)
if not os.path.exists(train_sharp_folder):
    os.makedirs(train_sharp_folder)
if not os.path.exists(val_blur_folder):
    os.makedirs(val_blur_folder)
if not os.path.exists(val_sharp_folder):
    os.makedirs(val_sharp_folder)

# 获取图像文件列表
image_files = os.listdir(blur_folder)
random.shuffle(image_files)  # 随机打乱文件列表

# 定义训练集和验证集的比例（例如80%训练，20%验证）
#train_ratio = 0.8
total_files = len(image_files)
print(total_files)
#train_count = int(total_files * train_ratio)
train_count = 9408

# 将数据分割为训练集和验证集
train_image_files = image_files[:train_count]                    
val_image_files = image_files[train_count:]

# 将图像和标签文件移动到对应的文件夹中
for image_file in train_image_files:
    label_file = os.path.splitext(image_file)[0] + ".jpg"  # 修改标签文件扩展名为.nii
    image_path = os.path.join(blur_folder, image_file)
    label_path = os.path.join(sharp_folder, label_file)

    # 移动DCM图像
    shutil.move(image_path, os.path.join(train_blur_folder, image_file))

    # 移动NIfTI标签文件
    shutil.move(label_path, os.path.join(train_sharp_folder, label_file))

for image_file in val_image_files:
    label_file = os.path.splitext(image_file)[0] + ".jpg"  # 修改标签文件扩展名为.nii
    image_path = os.path.join(blur_folder, image_file)
    label_path = os.path.join(sharp_folder, label_file)

    # 移动DCM图像
    shutil.move(image_path, os.path.join(val_blur_folder, image_file))

    # 移动NIfTI标签文件
    shutil.move(label_path, os.path.join(val_sharp_folder, label_file))

print("训练集和验证集建立完成。")
