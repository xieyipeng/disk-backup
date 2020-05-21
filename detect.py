import time
import psutil
import re
import os

flag = 'disk-backup.xieyipeng'


def detect():
    """
    功能说明：检测磁盘变动
    """
    try:
        while True:
            for disk in psutil.disk_partitions():
                if 'removable' in disk.opts:
                    driver, opts = disk.device, disk.opts  # 卷标，是否移动U盘
                    if flag in os.listdir(driver):
                        if 'cache' not in os.listdir(driver):
                            os.mkdir(os.path.join(driver, 'cache'))
                            print('ok')
                        print(os.path.join(driver))
                        print(os.listdir(driver))

            time.sleep(5)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    detect()
