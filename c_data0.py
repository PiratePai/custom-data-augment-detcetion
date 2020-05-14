import os
import random
from FsDs import generate_dir, random_choice, hms_string
import glob
import datetime
import shutil

# It is used to create data0
if __name__ == '__main__':
    rightnow_path = os.getcwd()  # 获取脚本当前目录路径
    label_path = os.path.join(rightnow_path, 'labels')  # 待读取label路径
    img_path = os.path.join(rightnow_path, 'img')  # 待读取img路径
    anno_path = os.path.join(rightnow_path, 'anno')  # 待读取xml路径
    start_time = datetime.datetime.now()
    ratio = 0.2  # 随机选取数据所占原数据的比例
    condition = 0
    generate_dir(condition, rightnow_path, ratio)
    print('Step2 DONE')
    end_time = datetime.datetime.now()
    seconds_elapsed = (end_time - start_time).total_seconds()
    print("It took {} to execute this".format(hms_string(seconds_elapsed)))
