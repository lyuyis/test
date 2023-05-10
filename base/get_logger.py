"""log日志封装"""
import logging.handles
class GetLogger():
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger()
            # 设置 日志器 级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理器 文件-以时间分割
            th = logging.handlers.TimedRotatingFileHandler(filename='./logtime02.log',
                                                           when='M',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s][%(filename)s (%(funcName)s:%(lineno)d]"
            fm = logging.Formatter(fmt)
            # 将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到 处理器 文件
            th.setFormatter(fm)
            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger

