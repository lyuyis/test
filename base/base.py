import time
from selenium.webdriver.support.wait import WebDriverWait
from po_calc.tool.get_log import get_logging

log = get_logging()

class Base:
    #初始化
    def __init__(self,driver):
        log.info('正在初始化浏览器对象 {}'.format(driver))
        self.driver = driver

    #查找元素，显式等待
    def base_find_element(self,loc,time=30,poll=0.5):
        """
        :param loc: 类型为元祖
        :param time: 等待时间
        :param poll: 访问频率
        :return: 返回元素
        """
        log.info('正在查找元素 {}'.format(loc))
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    #点击元素
    def base_click(self,loc):
        log.info('正在点击元素 {}'.format(loc))
        self.base_find_element(loc).click()

    #获取元素信息
    def base_get_value(self,loc):
        log.info('正在获取元素 {} 的值'.format(loc))
        return self.base_find_element(loc).get_attribute('value')

    #截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file('../img/{}.png'.format(time.strftime('%Y_%m_%d %H_%M_%S')))

