import time
import psutil
import os
import shutil

flag = 'disk-backup.ini'
cache_files = []
sub_size = 6


def my_sub(c_root_path, d_root_path):
    d = len(d_root_path)
    c = len(c_root_path)
    return c, d


def detect():
    """
    """
    while True:
        # TODO: 检测磁盘变动
        driver, opts = '', ''
        have_disk = False
        for disk in psutil.disk_partitions():
            if 'removable' in disk.opts:
                driver, opts = disk.device, disk.opts  # 卷标，是否移动U盘
                if flag in os.listdir(driver):
                    have_disk = True
                    break
        if have_disk:
            d_cache_path = os.path.join(driver, 'cache')
            # TODO: 检测是否有缓存文件夹
            if 'cache' not in os.listdir(driver):
                os.mkdir(os.path.join(driver, 'cache'))
            # TODO: 获取电脑上缓存文件夹路径
            temp = os.path.join(driver, flag)
            with open(temp, 'r', encoding='utf-8') as f:
                c_cache_path = f.readlines()[0]
            c, d = my_sub(c_cache_path[0:-5], os.path.join(driver))
            print(c, d)

            # TODO: 将c-cache下的文件列表存放到数组
            c_list, c_dirs = get_list(c, c_cache_path)

            # TODO: 将d-cache下的文件列表存放到数组
            d_list, d_dirs = get_list(d, d_cache_path)

            # print(c_list)
            # print(d_list)

            # TODO: 两个数组比较，找出缺少的文件
            lack_file = []
            get_lack_file(c_list, d_list, lack_file)
            print('lack:')
            print(lack_file)
            # TODO: copy
            # TODO: 创建电脑缓冲区存在的文件夹
            for dir in c_dirs:
                try:
                    os.mkdir(os.path.join(d_cache_path, dir[d + sub_size:]))
                except Exception as e:
                    print(e)

            for cp_file in lack_file:
                source = os.path.join(c_cache_path[0:-5], cp_file)
                target = os.path.join(driver, cp_file)
                try:
                    shutil.copy(source, target)
                    print('copy file: ', source)
                except Exception as e:
                    print(e)
        time.sleep(5)


def get_lack_file(c_list, d_list, lack_file):
    for c_file in c_list:
        if c_file not in d_list:
            lack_file.append(c_file)


def get_list(c, c_cache_path):
    list = []
    _dirs = []
    for root, dirs, files in os.walk(c_cache_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for f in files:
            list.append(str(os.path.join(root, f))[c:])
        for dir in dirs:
            # print(root,dir)
            _dirs.append(os.path.join(root, dir))
    return list, _dirs


def copy():
    pass


if __name__ == '__main__':
    detect()
