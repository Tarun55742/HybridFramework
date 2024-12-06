import time
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DD_Login:

    baseUrl = ReadConfig.getApplicationUrl()
    path = "./TestData/TestingData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("****** Test_002_DD_Login ******")
        self.logger.info("****** Verifying Login DDT Test ******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = Login(self.driver)
        self.rows= XLUtils.getRowCount(self.path,'Sheet1')
        self.column = XLUtils.getColumnCount(self.path,'Sheet1')
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            act_url = self.driver.current_url
            exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

            if act_url == exp_url:
                if self.exp == "Pass":
                    self.logger.info("*** Test Case Pass ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*** Test Case Fail ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_url != exp_url:
                if self.exp == "Pass":
                    self.logger.info("*** Test Case Failed ***")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*** Test Case Pass ***")
                    lst_status.append("Pass")
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test case is passed")
            print("Test DDT is passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test case is Failed")
            print("Test DDT is Failed")
            self.driver.close()
            assert False
        print("End of DD test case")






















