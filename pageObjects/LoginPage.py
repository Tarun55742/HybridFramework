from selenium.webdriver.common.by import By


class Login:
    textbox_username_name='username'
    textbox_password_name='password'
    button_login_xpath="//button[@type='submit']"
    link_prelogout_icon = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    link_logout_linktext='Logout'


    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(by=By.NAME,value=self.textbox_username_name).clear()
        self.driver.find_element(by=By.NAME, value=self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(by=By.NAME, value=self.textbox_password_name).clear()
        self.driver.find_element(by=By.NAME, value=self.textbox_password_name).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(by=By.XPATH,value=self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(by=By.XPATH, value=self.link_prelogout_icon).click()
        self.driver.find_element(by=By.LINK_TEXT, value=self.link_logout_linktext).click()