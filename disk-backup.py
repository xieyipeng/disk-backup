import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *

c_cache_path = '电脑本地缓存路径：'


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.resize(600, 400)
        self.setWindowTitle("服务安装")

        self.c_folder = QLabel(c_cache_path, self)
        self.c_folder.resize(200, 15)
        self.c_folder.move(30, 30)
        choose_c_folder_btn = QPushButton(self)
        choose_c_folder_btn.setText('选择电脑上的缓存路径')
        choose_c_folder_btn.move(30, 60)
        choose_c_folder_btn.clicked.connect(self.c_choose_folder)

        self.cb = QComboBox(self)
        self.cb.resize(100, 25)
        self.cb.move(30, 160)
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.currentIndexChanged.connect(self.selectionchange)
        detect_disk = QPushButton(self)
        detect_disk.setText('检测移动磁盘')
        detect_disk.move(30, 120)
        detect_disk.clicked.connect(self.detect_disk)

    def c_choose_folder(self):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        if directory[-5:] != 'cache':
            QMessageBox.information(self, 'Warning', '缓存文件夹必须命名为\'cache\'')
        else:
            temp = c_cache_path + directory
            print(temp)
            self.c_folder.setText(temp)

    def detect_disk(self):
        print(self.cb.currentText())

    def selectionchange(self, i):
        # 标签用来显示选中的文本
        # currentText()：返回选中选项的文本
        print('Items in the list are:')
        # 输出选项集合中每个选项的索引与对应的内容
        # count()：返回选项集合中的数目
        for count in range(self.cb.count()):
            print('Item' + str(count) + '=' + self.cb.itemText(count))
            print('current index', i, 'selection changed', self.cb.currentText())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = Main()
    my.move(300, 300)
    my.show()
    sys.exit(app.exec_())
