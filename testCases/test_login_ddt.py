import time

import pytest

from pajeObjects.LoginPage import Login
from utilities.customLogger import logGen
from utilities.readProperties import read_config
from utilities import ExcelUtils



class Test_001_Login:
    baseURL = read_config.geturl()
    logger = logGen.loggen()
    path = ".//TestData//Data.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info('*************************************************************************')
        self.logger.info('----------test_login_ddt STARTED----------')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info('----------Application URL opened----------')
        self.lp = Login(self.driver)
        self.rows = ExcelUtils.getRowcount(self.path,'Sheet1')
        print(self.rows)
        for r in range(2,self.rows-1):
            self.user = ExcelUtils.readData(self.path,'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path,'Sheet1', r, 2)
            self.result = ExcelUtils.readData(self.path, 'Sheet1', r , 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            time.sleep(3)
            self.lp.clickLogin()
            act_title = "Dashboard / nopCommerce administration"
            exp_title = self.driver.title
            if act_title == exp_title:
                if self.result == "pass":
                    assert True
                    self.lp.clickLogout()
                else:
                    self.lp.clickLogout()
                    assert False
            elif act_title != exp_title:
                if self.result == "fail":
                    assert True
                else:
                    assert False
        self.driver.close()
