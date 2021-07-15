import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//TestData//LoginData.xlsx"
    l = LogGen.runmethod()

    def test_Login(self, setup):
        self.l.info("************ Test_002_DDT_Login ************")
        self.l.info("************ Login Page DDT validation ************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.row = XLUtils.getRowCount(self.path,"Sheet1")
        lst_status = []
        print("Number of Rows ",self.row)
        for r in range(2,self.row+1):
            time.sleep(5)
            self.driver.get(self.baseUrl)
            self.username = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            if self.exp=="Pass":
                Pg_Title = self.driver.title
                if Pg_Title == "Dashboard / nopCommerce administration":
                    lst_status.append("Pass")
                    self.l.info("************ Login Page Title verified ************")
                    self.lp.clickLogout()
                    XLUtils.writeData(self.path,"Sheet1",r,4,"PASS")
                    assert True
                    # self.driver.close()
                else:
                    lst_status.append("Fail")
                    self.l.error("************ Login Page Title not verified ************")
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
                    # self.driver.close()
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "FAIL")
                    assert False
            if self.exp == "Fail":
                Pg_Title = self.driver.title
                if Pg_Title != "Dashboard / nopCommerce administration":
                    lst_status.append("Pass")
                    self.l.info("************ Login Page not displayed ************")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "PASS")
                    assert True
                    # self.driver.close()
                else:
                    lst_status.append("Fail")
                    self.l.error("************ Login Page Title verified ************")
                    self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "FAIL")
                    # self.driver.close()
                    assert False
            if "Fail" not in lst_status:
                self.l.info("************* DDT Test is Passed ***************")
            else:
                self.l.error("************* DDT Test is Failed ***************")
