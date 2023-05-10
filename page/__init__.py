from selenium.webdriver.common.by import By

"""计算机网址"""
page_url = 'http://cal.apple886.com/'

"""计算机配置信息"""
#输入数字
# for i in str(num):
#     page_input_num = By.ID, 'simple{}'.format(i)

#加法
calc_add = By.ID , 'simpleAdd'

#等号
calc_equal = By.ID, 'simpleEqual'

#运算结果
calc_res = By.ID, 'resultIpt'

#清屏
calc_clear = By.ID, 'simpleClearAllBtn'
