from selenium.webdriver.common.by import By

class AddUser:
    link_pim_xpath = "//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]/span[1]"
    btn_addnew_xpath= "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    txt_firstname_name= "firstName"
    txt_middilename_name= "middleName"
    txt_lastname_name = "lastName"
    txt_employeeid_xpath= "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
    btn_save_xpath= "//button[text()=' Save ']"


    def __init__(self,driver):
        self.driver = driver

    def clickAdmin(self):
        self.driver.find_element(by=By.XPATH, value=self.link_pim_xpath).click()

    def clickAddbtn(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_addnew_xpath).click()

    def setFirstName(self,firstname):
        self.driver.find_element(by=By.NAME, value=self.txt_firstname_name).send_keys(firstname)

    def setMiddleName(self,midname):
        self.driver.find_element(by=By.NAME, value=self.txt_middilename_name).send_keys(midname)

    def setLastName(self,lastname):
        self.driver.find_element(by=By.NAME, value=self.txt_lastname_name).send_keys(lastname)

    def setEmployeeID(self,empid):
        self.driver.find_element(by=By.XPATH,value=self.txt_employeeid_xpath).clear()
        self.driver.find_element(by=By.XPATH, value=self.txt_employeeid_xpath).send_keys(empid)

    def clickSave(self):
        self.driver.find_element(by=By.XPATH, value=self.btn_save_xpath).click()