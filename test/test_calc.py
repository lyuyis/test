import unittest
from po_calc.page.page_calc import PageCalc
from po_calc.base.get_driver import GetDriver
from parameterized import parameterized
from po_calc.tool.get_log import get_logging
from po_calc.tool.read_json import read_json

log = get_logging()

def get_data():
    arrs = []
    datas = read_json('calc.json')
    for data in datas.values():
        arrs.append((data.get('a'), data.get('b'), data.get('expect')))
    return arrs

class TestCalc(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.calc = PageCalc(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_calc(self,a,b,expect):
        self.calc.page_calc(a,b)
        try:
            #从json传过来的预期结果需要转成字符串类型再判断是否相等
            self.assertEqual(self.calc.page_get_res(),str(expect))
        except Exception as e:
            self.calc.page_get_img()
            log.error(e)

