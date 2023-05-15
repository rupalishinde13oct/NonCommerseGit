import time

from pageObjects.Login import LoginPage


class TestLogin:

    def test_Login_002(self , setup):

        self.d = setup

        self.lp = LoginPage(self.d)
        time.sleep(4)
        self.lp.Enter_Email("admin@yourstore.com")
        time.sleep(4)
        self.lp.Enter_Password("admin")
        self.lp.Click_On_LoginButton()
        time.sleep(5)
        self.lp.Click_On_LogoutButton()
