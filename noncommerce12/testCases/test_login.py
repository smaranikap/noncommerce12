import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    l = LogGen.runmethod()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.l.info("************ Test_001_Login ************")
        self.l.info("************ verify Home Page title ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.l.info("************ Home page title Tcs is passed *******""*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.l.info("************ Home page title Tcs is failed ************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Login(self, setup):
        self.l.info("************ Test_001_Login ************")
        self.l.info("************ Login Page validation ************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        Pg_Title = self.driver.title
        if Pg_Title == "Dashboard / nopCommerce administration":
            self.l.info("************ Login Page Title verified ************")
            assert True
            self.driver.close()
        else:
            self.l.error("************ Login Page Title not verified ************")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.driver.close()
            assert False



