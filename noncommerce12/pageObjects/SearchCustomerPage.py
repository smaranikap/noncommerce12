from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class SearchCustomer:
    txt_SearchEmail_Id = "SearchEmail"
    txt_SearchFirstname_Id = "SearchFirstName"
    txt_SearchLastname_Id = "SearchLastName"
    txt_SearchDateofbirth_Month_Id = "SearchMonthOfBirth"
    txt_SearchDateofbirth_Date_Id = "SearchDayOfBirth"
    txt_SearchCompany_Id = "SearchCompany"
    txt_SearchIPaddress_Id = "SearchIpAddress"
    txt_SearchIPCustomerroles_Id = "SearchFirstName"
    btn_Search_Id = "search-customers"
    tab_Customer_xpath = "//table[@id='customers-grid']//tbody"
    tabRow_Customer_xpath = "//table[@id='customers-grid']//tbody/tr"

    def __init__(self,driver):
        self.driver = driver

    def searchEmailid(self,EmailId):
        self.driver.find_element_by_id(self.txt_SearchEmail_Id).clear()
        self.driver.find_element_by_id(self.txt_SearchEmail_Id).send_keys(EmailId)

    def searchFirstname(self,Firstname):
        self.driver.find_element_by_id(self.txt_SearchEmail_Id).clear()
        self.driver.find_element_by_id(self.txt_SearchEmail_Id).send_keys(Firstname)

    def searchButton(self):
        self.driver.find_element_by_id(self.btn_Search_Id).click()

    def searchResultValidation(self,Emailid):
        searchResultValidation = 0
        tab = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.XPATH, self.tab_Customer_xpath)))
        Rowc = len(self.driver.find_elements_by_xpath(self.tabRow_Customer_xpath))

        time.sleep(5)
        for i in range(1, Rowc + 1):
            Colc = len(self.driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr[" + str(i) + "]/td"))
            for j in range(1, Colc):
                xp = "//table[@id='customers-grid']//tbody/tr[" + str(i) + "]/td[" + str(j) + "]"
                var = self.driver.find_element_by_xpath(xp).get_attribute('innerText')
                if var == Emailid:
                    print("Exist")
                    searchResultValidation=1
                    return searchResultValidation
                    break
                else:
                    searchResultValidation = 0










