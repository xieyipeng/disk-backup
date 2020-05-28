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


def test():
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
            create_cache(driver)
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

            # TODO: 两个数组比较，找出缺少的文件
            lack_file = get_lack_file(c_list, d_list)

            print('lack:')
            print(lack_file)
            # TODO: 创建电脑缓冲区存在的文件夹
            create_d_cache(c_dirs, d, d_cache_path)

            # TODO: copy
            copy(c_cache_path, driver, lack_file)
        time.sleep(5)


def copy(c_cache_path, driver, lack_file):
    """
    拷贝文件
    :param c_cache_path: 电脑缓冲区路径
    :param driver: 磁盘驱动卷标
    :param lack_file: 缺失文件列表
    :return: None
    """
    for cp_file in lack_file:
        source = os.path.join(c_cache_path[0:-5], cp_file)
        target = os.path.join(driver, cp_file)
        try:
            shutil.copy(source, target)
            print('copy file: ', source)
        except Exception as e:
            print(e)


def create_d_cache(c_dirs, d, d_cache_path):
    """
    在磁盘上创建文件路径
    :param c_dirs: 电脑缓冲区内的文件夹列表
    :param d: 磁盘路径差值
    :param d_cache_path: 磁盘缓冲区路径
    :return: None
    """
    for dir in c_dirs:
        try:
            os.mkdir(os.path.join(d_cache_path, dir[d + sub_size:]))
        except Exception as e:
            print(e)


def create_cache(driver):
    """
    如果磁盘上没有cache文件夹，则创建
    :param driver: 磁盘的卷标
    :return: None
    """
    if 'cache' not in os.listdir(driver):
        os.mkdir(os.path.join(driver, 'cache'))


def get_lack_file(c_list, d_list, ):
    """
    对比电脑上缓冲区与磁盘上缓冲区内的文件，将磁盘缓冲区内缺少的文件找出
    :param c_list: 电脑缓冲区所有文件
    :param d_list: 磁盘缓冲区所有文件
    :return: 磁盘缓冲区缺少的文件
    """
    lack_file = []
    for c_file in c_list:
        if c_file not in d_list:
            lack_file.append(c_file)
    return lack_file


def get_list(sub, cache_path):
    """
    获取缓冲区内地文件列表
    :param sub: 差值
    :param cache_path: 缓存路径
    :return: 路径下所有文件名称的列表，路径下所有文件夹名称列表
    """
    _list = []
    _dirs = []
    for root, dirs, files in os.walk(cache_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for f in files:
            _list.append(str(os.path.join(root, f))[sub:])
        for dir in dirs:
            # print(root,dir)
            _dirs.append(os.path.join(root, dir))
    return _list, _dirs


if __name__ == '__main__':
    test()
