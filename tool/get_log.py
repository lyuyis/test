import logging

def get_logging():
    fm = "%(asctime)s %(levelname)s [%(name)s][%(filename)s (%(funcName)s:%(lineno)d]"
    logging.basicConfig(level=logging.INFO,format=fm,filename='../log/log01.log')
    return logging