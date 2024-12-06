import random
import pytest
from selenium.webdriver.common.by import By
from pageObjects.AddUserPage import AddUser
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_003_AddPIM:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addpim(self,setup):
        self.logger.info("****** Test_003_addpim ****** ")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("** Login Successful **")



        self.logger.info("** Started adding PIM**")
        self.addEmp = AddUser(self.driver)
        self.addEmp.clickAdmin()
        time.sleep(5)
        self.addEmp.clickAddbtn()
        time.sleep(5)
        self.logger.info("** Started sending employee details **")
        self.addEmp.setFirstName("Tarun")
        self.addEmp.setMiddleName("Kumar")
        self.addEmp.setLastName("Vedwan")
        self.random = random.randint(1000,100000)
        self.addEmp.setEmployeeID(self.random)

        self.logger.info("** Clicking on save button **")
        self.addEmp.clickSave()
        self.logger.info("** User added Successfully **")
        time.sleep(5)
        self.text = self.driver.find_element(by=By.XPATH, value="//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']").text
        print(self.text)
        time.sleep(5)

        if self.text=="Personal Details":
            assert True
            self.logger.info("** Test case Passed **")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addpim.png")
            assert False

        self.driver.close()
        self.logger.info("** Test case Passed **")



