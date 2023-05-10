from selenium import webdriver
from po_calc.page import page_url

"""单例模式   保证只有一个driver对象"""
class GetDriver():
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page_url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            #此时driver的值不为空
            cls.driver = None


