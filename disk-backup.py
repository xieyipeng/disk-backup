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

        self.c_path = None
        self.d_ok = False

        self.c_folder = QLabel(c_cache_path, self)
        self.c_folder.resize(200, 15)
        self.c_folder.move(30, 30)
        choose_c_folder_btn = QPushButton(self)
        choose_c_folder_btn.setText('选择电脑上的缓存路径')
        choose_c_folder_btn.move(30, 60)
        choose_c_folder_btn.clicked.connect(self.c_choose_folder)

        self.cb = QComboBox(self)
        self.cb.resize(150, 25)
        self.cb.move(30, 160)
        self.cb.currentIndexChanged.connect(self.selectionchange)
        detect_disk = QPushButton(self)
        detect_disk.setText('检测移动磁盘')
        detect_disk.move(30, 120)
        detect_disk.clicked.connect(self.detect_disk)

        d_create_folder = QPushButton(self)
        d_create_folder.setText('创建cache和flag')
        d_create_folder.move(30, 210)
        d_create_folder.clicked.connect(self.create_d_folder)

        install = QPushButton(self)
        install.setText('安装服务')
        install.move(460, 210)
        install.clicked.connect(self.install_service)

        install = QPushButton(self)
        install.setText('启动服务')
        install.move(460, 250)
        install.clicked.connect(self.start_service)

        install = QPushButton(self)
        install.setText('停止服务')
        install.move(460, 290)
        install.clicked.connect(self.stop_service)

        uninstall = QPushButton(self)
        uninstall.setText('删除服务')
        uninstall.move(460, 330)
        uninstall.clicked.connect(self.uninstall_service)

    def stop_service(self):
        run_command(self, 'python main.py stop')

    def start_service(self):
        try:
            os.system('python main.py start')
        except Exception as e:
            QMessageBox.information(self, 'Warning', e)

    def install_service(self):
        # try:
        #     os.system('python main.py install')
        # except Exception as e:
        #     QMessageBox.information(self, 'Warning', e)
        run_command('python main.py install')

    def uninstall_service(self):
        try:
            os.system('python main.py uninstall')
        except Exception as e:
            QMessageBox.information(self, 'Warning', e)

    def create_d_folder(self):
        driver = self.cb.currentText()
        print(driver)
        if self.c_path is None:
            QMessageBox.information(self, 'Warning', '请选择电脑缓存路径！')
            return
        if driver == '':
            QMessageBox.information(self, 'Warning', '请先选择磁盘！')
            return
        try:
            os.mkdir(driver[0:-14] + 'cache')
            with open(os.path.join(driver[0:-14] + 'disk-backup.ini'), 'w', encoding='utf-8') as f:
                f.writelines(self.c_folder.text()[9:])
            QMessageBox.information(self, 'Warning', '成功创建：cache文件夹以及disk-backup.ini！')
            self.d_ok = True
        except Exception as e:
            QMessageBox.information(self, 'Warning', str(e))

    def c_choose_folder(self):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        if directory[-5:] != 'cache':
            QMessageBox.information(self, 'Warning', '缓存文件夹必须命名为\'cache\'')
        else:
            temp = c_cache_path + directory
            self.c_path = directory
            print(self.c_path)
            self.c_folder.setText(temp)

    def detect_disk(self):
        self.cb.clear()
        for disk in disk_partitions():
            if 'removable' in disk.opts:
                driver, opts = disk.device, disk.opts  # 卷标，是否移动U盘
                self.cb.addItem(driver + '(' + opts + ')')

    def selectionchange(self, i):
        for count in range(self.cb.count()):
            print('项目' + str(count) + '=' + self.cb.itemText(count))
            print('当前序号：', i, '选项改变：', self.cb.currentText())


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_command(self, com):
    try:
        if is_admin():
            os.system(com)
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            else:
                ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    except Exception as e:
        QMessageBox.information(self, 'Warning', e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = Main()
    my.move(300, 300)
    my.show()
    sys.exit(app.exec_())
