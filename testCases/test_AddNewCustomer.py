import random
import string
import time

import pytest

from pajeObjects.AddNewCustomer import AddCustomer
from pajeObjects.LoginPage import Login
from utilities.readProperties import read_config


class Test_AddCustomer:
    baseURL= read_config.geturl()
    userName = read_config.getusername()
    passWord = read_config.getpassword()

    @pytest.mark.sanity
    def test_addNewCustomer(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.passWord)
        self.lp.clickLogin()

        self.ac = AddCustomer(self.driver)
        self.ac.click_on_customer()
        self.ac.click_on_subCustomer()
        self.ac.click_addNew()
        self.email = random_generator() + "@gmail.com"
        self.ac.setEmail(self.email)
        self.ac.setFirstName("Someswar")
        self.ac.setLastName("Salana")
        self.ac.setCustmorRole("Guests")
        self.ac.click_SveBtn()









def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
   return ''.join(random.choice(chars) for x in range(size))