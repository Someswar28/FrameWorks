import time


class Search_by_Email:
    email_result = "//*[@id='customers-grid']/tbody/tr/td[2]"
    name_result = "//*[@id='customers-grid']/tbody/tr/td[3]"
    txtbox_search_email = "//*[@id='SearchEmail']"
    btn_search = "//*[@id='search-customers']"
    txt_searchFirstName = "//*[@id='SearchFirstName']"
    txt_searchLastName  = "//*[@id='SearchLastName']"

    def __init__(self,driver):
        self.driver = driver

    def verify_by_email(self,email):
        self.driver.find_element_by_xpath(self.txtbox_search_email).send_keys(email)
        self.driver.find_element_by_xpath(self.btn_search).click()
        time.sleep(3)
        self.msg = self.driver.find_element_by_xpath(self.email_result).text
        if self.msg == "victoria_victoria@nopCommerce.com":
            assert True
        else:
            assert False

        self.driver.close()

    def verify_by_Name(self,fname,lname):
        self.driver.find_element_by_xpath(self.txt_searchFirstName).send_keys(fname)
        self.driver.find_element_by_xpath(self.txt_searchLastName).send_keys(lname)
        self.driver.find_element_by_xpath(self.btn_search).click()
        time.sleep(3)
        self.msg = self.driver.find_element_by_xpath(self.name_result).text
        if self.msg == "Victoria Terces":
            assert True
        else:
            assert False

        self.driver.close()

