from selenium.webdriver.common.by import By


class LoginPage:

    Email_XPATH = (By.XPATH , "//input[@id='Email']")
    Password_XPATH = (By.XPATH , "//input[@id='Password']")
    LoginButton_XPATH = (By.LINK_TEXT , "Log in")
    Logout_XPATH = (By.LINK_TEXT , "Logout")

    def __init__(self , d):
        self.d = d

    def Enter_Email(self , email):
        self.d.find_element(*LoginPage.Email_XPATH).send_keys(email)

    def Enter_Password(self , password):
        self.d.find_element(*LoginPage.Password_XPATH).send_keys(password)

    def Click_On_LoginButton(self):
        self.d.find_element(*LoginPage.LoginButton_XPATH).click()

    def Click_On_LogoutButton(self):
        self.d.find_element(*LoginPage.Logout_XPATH).click()