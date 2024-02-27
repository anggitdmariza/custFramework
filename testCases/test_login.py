import pageObjects.login_page
from utilities.log_gen import LogsGen
from utilities.read_prop import ReadConfig


class TestLogin:
    baseurl = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogsGen.logs()

    def test_001_login(self, setup):
        self.logger.info("Starting test_001_login")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        assert "Your store. Login" in act_title
        self.driver.save_screenshot("./Screenshots/login_page.png")
        self.logger.info("Succesfully get into login page")
        self.lp = pageObjects.login_page.Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        assert "Dashboard / nopCommerce administration" in act_title
        self.driver.save_screenshot('./Screenshots/dashboard.png')
        self.logger.info("Succesfully get into dashboard page")
        self.lp.click_logout()
        self.driver.close()
        self.logger.info("End test_001_login")


if __name__ == "__main__":
    TestLogin()
