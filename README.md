# disk-backup
u盘备份

细节：

1. windows创建服务




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