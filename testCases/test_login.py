import pytest

from pajeObjects.LoginPage import Login
from utilities.customLogger import logGen
from utilities.readProperties import read_config


class Test_001_Login:
    baseURL = read_config.geturl()
    username = read_config.getusername()
    password = read_config.getpassword()
    logger = logGen.loggen()
    @pytest.mark.sanity
    def test_HomePageTitle(self, setup):
        self.logger.info('----------test_HomePageTitle STARTED----------')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info('----------Application URL opened----------')
        act_title = self.driver.title
        exp_title = "Your store. Login"
        if act_title == exp_title:
            self.logger.info('----------test_HomePageTitle PASSED----------')
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_HomePageTitle.png")
            self.logger.error('----------test_HomePageTitle FAILED----------')
            self.driver.close()
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('*************************************************************************')
        self.logger.info('----------test_login FAILED----------')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info('----------Application URL opened----------')
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.logger.info('----------Username enter successfully----------')
        self.lp.setPassword(self.password)
        self.logger.info('----------Password enter successfully----------')
        self.lp.clickLogin()
        self.logger.info('----------Login successfully----------')
        exp_title = "Dashboard / nopCommerce administration"
        act_title = self.driver.title
        if act_title == exp_title:
            self.lp.clickLogout()
            self.logger.info('----------LogOut successfully----------')
            self.logger.info('----------test_login PASSED----------')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.logger.info('----------test_login FAILED----------')
            self.driver.close()
            assert False

