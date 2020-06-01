import ctypes
import os
import sys

from PyQt5 import QtWidgets
from psutil import disk_partitions
from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox, QWidget, QMessageBox, QFileDialog
from numpy import unicode

c_cache_path = '电脑本地缓存路径：'
flag = 'disk-backup.ini'


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.resize(600, 400)
        self.setWindowTitle("服务安装")

        detect_disk = QPushButton(self)
        detect_disk.setText('检测移动磁盘')
        detect_disk.move(30, 120)
        detect_disk.clicked.connect(self.detect_disk)

    def detect_disk(self):
        print('123')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = Main()
    my.move(300, 300)
    my.show()
    sys.exit(app.exec_())
