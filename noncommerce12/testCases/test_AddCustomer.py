import pytest
from pageObjects.AddCustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomer
import random

class Test_001_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    l = LogGen.runmethod()

    @pytest.mark.sanity
    @pytest.mark.a
    def test_addnewCustomer(self,setup):
        self.l.info("************ Test_001_AddCustomer ************")
        self.l.info("************ Adding New Customer details ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.cp = CustomerPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp.click_CustomerMenu()
        self.cp.click_CustomerSubmenu()
        self.cp.click_AddNew()
        self.l.info("************ started feeding data for new customer ************")
        n = random.randrange(1, 1000)
        email = "Testing_" + str(n) + "@gmail.com"
        self.cp.set_Email(email)
        self.cp.set_Password('login@123')
        self.cp.set_FirstName('Testing1')
        self.cp.set_LastName('test1')
        self.cp.click_Gender()
        self.cp.select_DateofBirth()
        self.cp.set_CompanyName('ITC infotech')
        self.cp.click_IsTaxExempt()
        self.cp.select_NewsLetter()
        self.cp.select_CustomerRole()
        self.cp.select_ManageofVender('Vendor 1')
        self.cp.set_Admincomment('testing comments')
        self.cp.click_Save()
        self.l.info("************ saving customer details ************")

    @pytest.mark.sanity
    def test_SearchCusomer_Emailid(self,setup):
        self.l.info("************ Test_001_AddCustomer ************")
        self.l.info("************ Search Customer details ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.cp = CustomerPage(self.driver)
        self.scp = SearchCustomer(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.cp.click_CustomerMenu()
        self.cp.click_CustomerSubmenu()
        self.scp.searchEmailid('victoria_victoria@nopCommerce.com')
        self.scp.searchButton()
        if self.scp.searchResultValidation('victoria_victoria@nopCommerce.com')==1:
            self.l.info("************ Email ID searched successfully ************")
        else:
            self.l.info("************ Email ID not exist in the table ************")


















