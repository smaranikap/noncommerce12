import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class CustomerPage:

    lnkCustomer_menu_xpath = "//i[@class='nav-icon far fa-user']"
    lnkCustomer_submenu_xpath = "//p[text()=' Customers']"
    btn_AddNew_Xpath = "//a[@class='btn btn-primary']"
    txt_Email_Id  = "Email"
    txt_Password_Id = "Password"
    txt_FirstName_Id = "FirstName"
    txt_LastName_Id = "LastName"
    chk_Gender_Id = "Gender_Male"
    lnk_CalenderIcon_Xpath = "//span[@class='k-icon k-i-calendar']"
    btn_CalendderDate_Linktext = "15"
    txt_Companyname_Id = "Company"
    chk_IsTaxExempt_Id = "IsTaxExempt"
    lstbox_NewsLetter_Xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    litem_NewsLetter_Xpath = "//li[text()='Test store 2']"
    lstbox_CustomerRole_Xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    litem_CustomerRole_Xpath = "//li[text()='Forum Moderators']"
    Select_Managerofvendor_id = "VendorId"
    txtarea_Admincomment_Xpath = "//textarea[@name='AdminComment']"
    btn_Save_Xpath = "//button[@name='save']"
    txt_Searchemail_id = "SearchEmail"
    btn_search_id = "search-customers"

    def __init__(self,driver):
        self.driver = driver

    def click_CustomerMenu(self):
        custmenu = WebDriverWait(self.driver,20).until(ec.visibility_of_element_located((By.XPATH,self.lnkCustomer_menu_xpath)))
        custmenu.click()
        # self.driver.find_element_by_xpath(self.lnkCustomer_menu_xpath).click()
    def click_CustomerSubmenu(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, self.lnkCustomer_submenu_xpath))).click()
        # self.driver.find_element_by_xpath(self.lnkCustomer_submenu_xpath).click()
    def click_AddNew(self):
        self.driver.find_element_by_xpath(self.btn_AddNew_Xpath).click()
    def set_Email(self,email):
        time.sleep(5)
        self.driver.find_element_by_id(self.txt_Email_Id).send_keys(email)
    def set_Password(self,password):
        self.driver.find_element_by_id(self.txt_Password_Id).send_keys(password)
    def set_FirstName(self,firstname):
        self.driver.find_element_by_id(self.txt_FirstName_Id).send_keys(firstname)
    def set_LastName(self,lastname):
        self.driver.find_element_by_id(self.txt_LastName_Id).send_keys(lastname)
    def click_Gender(self):
        self.driver.find_element_by_id(self.chk_Gender_Id).click()
    def select_DateofBirth(self):
        ele = WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH,self.lnk_CalenderIcon_Xpath)))
        ele.click()
        # self.driver.find_element_by_id(self.lnk_CalenderIcon_Xpath).click()
        time.sleep(5)
        self.driver.find_element_by_link_text(self.btn_CalendderDate_Linktext).click()
    def set_CompanyName(self,companyname):
        self.driver.find_element_by_id(self.txt_Companyname_Id).send_keys(companyname)
    def click_IsTaxExempt(self):
        self.driver.find_element_by_id(self.chk_IsTaxExempt_Id).click()
    def select_NewsLetter(self):
        self.driver.find_element_by_xpath(self.lstbox_NewsLetter_Xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.litem_NewsLetter_Xpath).click()
    def select_CustomerRole(self):
        self.driver.find_element_by_xpath(self.lstbox_CustomerRole_Xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.litem_CustomerRole_Xpath).click()
    def select_ManageofVender(self,item):
        Select(self.driver.find_element_by_id(self.Select_Managerofvendor_id)).select_by_visible_text(item)
    def set_Admincomment(self,comments):
        self.driver.find_element_by_xpath(self.txtarea_Admincomment_Xpath).send_keys(comments)
    def click_Save(self):
        self.driver.find_element_by_xpath(self.btn_Save_Xpath).click()
















