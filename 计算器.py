

from appium import webdriver
from time import *
import unittest

def peizhi():
    config = {}
    config['platformName'] = 'android'
    config['platformVersion'] = '5.1.1'
    config['deviceName'] = 'OPPO R11'
    config['deviceVersion'] = '127.0.0.1:62001'
    config['appPackage'] = 'com.xgzz.calculator'
    config['appActivity'] = 'com.simplemobiletools.calculator.activities.MainActivity'
    return config

def fengzhuang_jia(self,a,b):
    sleep(2)
    self.driver.find_element_by_id(a).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_plus').click()
    sleep(2)
    self.driver.find_element_by_id(b).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_equals').click()
    sleep(2)
    result = self.driver.find_element_by_id('com.xgzz.calculator:id/result').text
    return result

def fengzhuang_jian(self,a,b):
    sleep(2)
    self.driver.find_element_by_id(a).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_minus').click()
    sleep(2)
    self.driver.find_element_by_id(b).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_equals').click()
    sleep(2)
    result = self.driver.find_element_by_id('com.xgzz.calculator:id/result').text
    return result

def fengzhuang_cheng(self,a,b):
    sleep(2)
    self.driver.find_element_by_id(a).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_multiply').click()
    sleep(2)
    self.driver.find_element_by_id(b).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_equals').click()
    sleep(2)
    result = self.driver.find_element_by_id('com.xgzz.calculator:id/result').text
    return result
def fengzhuang_chu(self,a,b):
    sleep(2)
    self.driver.find_element_by_id(a).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_divide').click()
    sleep(2)
    self.driver.find_element_by_id(b).click()
    sleep(2)
    self.driver.find_element_by_id('com.xgzz.calculator:id/btn_equals').click()
    sleep(2)
    result = self.driver.find_element_by_id('com.xgzz.calculator:id/result').text
    return result


class JiSuanQi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',peizhi())
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_jia(self):
        #1+2
        jiafa = fengzhuang_jia(self,'com.xgzz.calculator:id/btn_1','com.xgzz.calculator:id/btn_2')
        print(jiafa)

    def test_jian(self):
        #4-2
        jianfa = fengzhuang_jian(self, 'com.xgzz.calculator:id/btn_4', 'com.xgzz.calculator:id/btn_2')
        print(jianfa)

    def test_cheng(self):
        #4*2
        chengfa = fengzhuang_cheng(self, 'com.xgzz.calculator:id/btn_4', 'com.xgzz.calculator:id/btn_2')
        print(chengfa)


if __name__ == '__main__':
    unittest.main()










