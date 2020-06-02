# disk-backup
u盘备份

* 细节：以安装服务的方式进行U盘备份

* 思路：在U盘与电脑上各创建文件夹，比对缺失文件，进行拷贝

### 使用

* 在磁盘根目录创建cache文件夹以及disk-backup.ini文件，cache文件是拷贝目标目录，disk-backup.ini是一个flag，标志该磁盘是不是自己的U盘，是否需要进行后续拷贝操作。

* 在disk-backup.ini中一行添加路径，该路径指向电脑上的cache目录。例如` D:/cache`

* 安装服务
```python
python main.py install # 安装
python main.py start # 启动
python main.py stop # 停止
python main.py remove # 移除
python main.py restart # 重启
```

* 拷贝日志记录在log文件夹下

### 总结

* python环境

```python
pip install pywin32
pip install pyinstaller
```

* 打包exe：项目目录下执行`pyinstaller -F -w disk-backup.py`生成exe文件（在dist文件夹下）

> 该exe文件**仅**用于创建电脑及移动磁盘上的cache文件以及flag

* 安装服务：项目目录下执行`python main.py install`(管理员权限)

* 遇到的问题：

> 在exe中将目录cd到main.py文件目录；

> 在exe中申请管理员权限运行安装服务命令；

> 打包disk-backup.py（界面）的同时将main.py（安装程序）打包起来

* python程序打包（在python36下可以打包成功）

```python
pyinstaller -F -w main.py
# 或者
pyinstaller -D -w main.py
```