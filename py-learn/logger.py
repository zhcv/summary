# coding: utf-8

import logging
import logging.handlers
from logging import *
from datetime import *

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

rht = logging.handlers.TimedRotatingFileHandler("reindex_out.log", 'D')
fmt = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(lineno)s %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
rht.setFormatter(fmt)
logger.addHandler(rht)

debug = logger.debug
info = logger.info
warning = logger.warn
error = logger.error
critical = logger.critical

"""
 %(levelno)s:     打印日志级别的数值
 %(levelname)s:   打印日志级别名称
 %(pathname)s:    打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s:    打印当前执行程序名
 %(funcName)s:    打印日志的当前函数
 %(lineno)d:      打印日志的当前行号
 %(asctime)s:     打印日志的时间
 %(thread)d:      打印线程ID
 %(threadName)s:  打印线程名称
 %(process)d:     打印进程ID
 %(message)s:     打印日志信息
"""
