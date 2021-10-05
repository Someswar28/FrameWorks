import pytest

from pajeObjects.AddNewCustomer import AddCustomer
from pajeObjects.LoginPage import Login
from pajeObjects.SearchPage import Search_by_Email
from utilities.readProperties import read_config


class Test_SearchByName:
    baseURL = read_config.geturl()
    userName = read_config.getusername()
    passWord = read_config.getpassword()

    @pytest.mark.regression
    def test_VerifyByName(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.passWord)
        self.lp.clickLogin()

        self.ac = AddCustomer(self.driver)
        self.ac.click_on_customer()
        self.ac.click_on_subCustomer()

        self.an = Search_by_Email(self.driver)
        self.an.verify_by_Name('Victoria', 'Terces')
