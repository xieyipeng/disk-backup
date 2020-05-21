import os
import win32serviceutil
import win32service
import win32event
import time
import inspect
from logging.handlers import TimedRotatingFileHandler
import logging


class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "disk-backup"
    _svc_display_name_ = "disk-backup-xieyipeng"
    _svc_description_ = "Automatic disk backup"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.T = time.time
        self.run = True

    def _getLogger(self):
        logger = logging.getLogger('[disk-backup]')
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        if os.path.isdir('%s\\log' % dirpath):  # 创建log文件夹
            pass
        else:
            os.mkdir('%s\\log' % dirpath)
        dir = '%s\\log' % dirpath

        handler = TimedRotatingFileHandler(os.path.join(dir, "test.log"), when="midnight", interval=1,
                                           backupCount=20)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        self.logger.error("svc do run...")
        try:
            while self.run:
                self.logger.error("I am alive.")
                time.sleep(5)
        except Exception as e:
            self.logger.info(e)

    def SvcStop(self):
        self.logger.error("svc do stop...")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件
        win32event.SetEvent(self.hWaitStop)
        self.run = False


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)

"""
1.安装服务
 
python PythonService.py install
 
2.让服务自动启动
 
python PythonService.py --startup auto install 
 
3.启动服务
 
python PythonService.py start
 
4.重启服务
 
python PythonService.py restart
 
5.停止服务
 
python PythonService.py stop
 
6.删除/卸载服务
 
python PythonService.py remove
"""

# CreateEvent
"""
LPSECURITY_ATTRIBUTES lpEventAttributes,　　// 安全属性
BOOL bManualReset, 　　　　　　　　　　　　　　// 复位方式　　
BOOL bInitialState, 　　　　　　　　　　　　　 // 初始状态 　　
LPCTSTR lpName　　
"""
