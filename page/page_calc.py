from selenium.webdriver.common.by import By
from po_calc.base.base import Base
from po_calc import page

class PageCalc(Base):
    #点击数字
    def page_input_num(self,num):
        for n in str(num):
            loc = By.ID,'simple{}'.format(n)
            self.base_click(loc)

    #点击加法
    def page_add(self):
        self.base_click(page.calc_add)

    def page_equal(self):
        self.base_click(page.calc_equal)

    #获取结果
    def page_get_res(self):
        return self.base_get_value(page.calc_res)

    #清屏
    def page_clear(self):
        self.base_click(page.calc_clear)

    #组装加法
    def page_calc(self,a,b):
        self.page_input_num(a)
        self.page_add()
        self.page_input_num(b)
        self.page_equal()

    def page_get_img(self):
        self.base_get_img()