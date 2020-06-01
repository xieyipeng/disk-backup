# disk-backup
u盘备份

细节：

1. windows创建服务
2. python程序打包

## 总结

* 环境

```python
pip install pywin32
pip install pyinstaller
```

* 项目目录下执行`pyinstaller -F -w disk-backup.py`生成exe文件（在dist文件夹下）

> 该exe文件用于创建电脑及移动磁盘上的cache文件以及flag

* 安装服务：项目目录下执行`python main.py install`(管理员权限)

* 遇到的问题：

> 在exe中将目录cd到main.py文件目录；

> 在exe中申请管理员权限运行安装服务命令；

> 打包disk-backup.py（界面）的同时将main.py（安装程序）打包起来


# 1、windows创建服务（测试）

* 文件目录：`../test`

* 关键方法

```python
self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

...
...
...

"""
@securityAttributes 安全属性
@bManualReset 复位方式
@bInitialState 初始状态
@name 对象名称
"""
handle = CreateEvent(securityAttributes, bManualReset, bInitialState, name)
```

* 使用

```python
python test.py install
python test.py start
python test.py stop
python test.py remove
python test.py restart
```

# 2、python程序打包（在python36下可以打包成功）

* 安装pyinstaller模块

```python
pip install pywin32
pip install pyinstaller
```

* 封装

```python
pyinstaller -F -w main.py
```

* 错误检查

```python
pyinstaller -D main.py
```