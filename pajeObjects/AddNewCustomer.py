import string
import time


class AddCustomer:
    lnk_customer ="//ul[contains(@class,'nav nav-pills')]/li[4]"
    lnk_sub_customer= "//ul[contains(@class,'nav nav-pills nav-sidebar')]/li[4]/ul/li"
    lnk_addNew = ".float-right a"
    txtbox_Email = "#Email"
    txtbox_FirstName = "#FirstName"
    txtbox_LastName = "#LastName"
    exit_option = "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[@title='delete']"
    drp_customerRole = "//div[@class='k-multiselect-wrap k-floatwrap']"
    msg_Administrators = "//li[text()='Administrators']"
    msg_ForumModerators = "//li[text()='Forum Moderators']"
    msg_Guests = "//li[text()='Guests']"
    msg_Registered = "//li[text()='Registered']"
    msg_Vendors = "//li[text()='Vendors']"
    btn_save = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customer(self):
        self.driver.find_element_by_xpath(self.lnk_customer).click()

    def click_on_subCustomer(self):

        self.driver.find_element_by_xpath(self.lnk_sub_customer).click()

    def click_addNew(self):
        self.driver.find_element_by_css_selector(self.lnk_addNew).click()

    def setEmail(self, Email):
        self.driver.find_element_by_css_selector(self.txtbox_Email).send_keys(Email)

    def setFirstName(self,FirstName):
        self.driver.find_element_by_css_selector(self.txtbox_FirstName).send_keys(FirstName)

    def setLastName(self,LastName):
        self.driver.find_element_by_css_selector(self.txtbox_LastName).send_keys(LastName)

    def setCustmorRole(self,role):
        self.drp = self.driver.find_element_by_xpath(self.drp_customerRole)
        self.driver.execute_script("arguments[0].click();", self.drp)
        if role == "Guests":
            self.driver.find_element_by_xpath(self.exit_option).click()
            self.button=self.driver.find_element_by_xpath(self.msg_Guests)
        elif role == "Administrators":
            self.button=self.driver.find_element_by_xpath(self.msg_Administrators)
        elif role == "ForumModerators":
            self.button=self.driver.find_element_by_xpath(self.msg_ForumModerators)
        elif role == "Vendors":
            self.button=self.driver.find_element_by_xpath(self.msg_Vendors)

        self.driver.execute_script("arguments[0].click();", self.button)

    def click_SveBtn(self):
        self.driver.find_element_by_xpath(self.btn_save).click()
        self.driver.close()






























































































































































































