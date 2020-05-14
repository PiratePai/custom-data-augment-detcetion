import os
import random
import glob
import datetime
import shutil

rightnow_path = os.getcwd()  # 获取脚本当前目录路径
label_path = os.path.join(rightnow_path, 'labels')  # 待读取label路径
img_path = os.path.join(rightnow_path, 'img')  # 待读取img路径
anno_path = os.path.join(rightnow_path, 'anno')  # 待读取xml路径


def hms_string(sec_elapsed):    # 格式化显示已消耗时间
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60.
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)
# 计时函数


def dele_h(list):  #  删除后缀
    new_list = []
    num = len(list)
    num_l = range(num)
    for i in num_l:
        new_list.append(list[i][:-4])
    return new_list#
# 删除后缀


def delef(path1, path2, path3):  # 删除不匹配项
    t_path1 = os.listdir(path1)
    t_path2 = os.listdir(path2)
    t_path3 = os.listdir(path3)
    n_list1 = dele_h(t_path1)
    n_list2 = dele_h(t_path2)
    n_list3 = dele_h(t_path3)
    # num_1 = len(n_list1)
    # print(num_1)
    for item in n_list1:
        if item not in n_list2:
            print('1&2 is not pair!')
        else:
            if item not in n_list3:
                print('1&3 is not pair!')
                r_path_1 = path1 + '/' + item + '.jpg'
                r_path_2 = path2 + '/' + item + '.xml'
                os.remove(r_path_1)
                os.remove(r_path_2)
    for item in n_list2:
        if item not in n_list1:
            print('1&2 is not pair!')
        else:
            if item not in n_list3:
                print('1&3 is not pair!')
                r_path_1 = path1 + '/' + item + '.jpg'
                r_path_2 = path2 + '/' + item + '.xml'
                os.remove(r_path_1)
                os.remove(r_path_2)
    print('1&2 is pair!')
# 匹配文件


def generate_dir(con, root_path, r):   # 往images和labels文件夹下生成相应的文件夹
    images_dir = os.path.join(root_path, 'img')  # 原有图片存储位置
    if con == 0:  # 生成data1文件夹：用于存放随机抽取的数据集
        new_data_dir = os.path.join(root_path, 'data')
        new_images_dir = os.path.join(new_data_dir, 'images')
        new_labels_dir = os.path.join(new_data_dir, 'labels')  # 将图片从原来的文件夹复制到该文件夹下

        if not os.path.exists(new_data_dir):
            os.makedirs(new_data_dir)

        if not os.path.exists(new_images_dir):
            os.makedirs(new_images_dir)

        total_test = os.listdir(new_images_dir)
        if len(total_test):
            return print('目标文件夹已存在文件，请删除后重试 ')

        if not os.path.exists(new_labels_dir):
            os.makedirs(new_labels_dir)

        get_sample = random_choice(images_dir, r)
        num_get = len(get_sample)
        list_get = range(num_get)
        for n in list_get:
            temp_img = get_sample[n]
            temp_label = temp_img.replace('img', 'labels')
            temp_label = temp_label.replace('jpg', 'txt')
            shutil.copy(temp_img, new_images_dir)
            shutil.copy(temp_label, new_labels_dir)


def random_choice(path, rr):
    t_path = os.listdir(path)
    n_list = dele_h(t_path)
    num_n = len(n_list)
    list_n = range(num_n)
    ti = int(num_n * rr)
    random_list = random.sample(list_n, ti)
    new_list = []
    for ir in list_n:
        if ir in random_list:
            new_path = os.path.join(path, t_path[ir])
            new_list.append(new_path)
    return new_list


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    # delef(imgfilepath, annofilepath, labelfilepath)  # 验证3文件夹数据是否匹配，删除不匹配文件
    print('Step1 done!')
    end_time = datetime.datetime.now()
    seconds_elapsed = (end_time - start_time).total_seconds()
    print("It took {} to execute this".format(hms_string(seconds_elapsed)))
