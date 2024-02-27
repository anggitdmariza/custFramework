import pageObjects.login_page
from utilities import XLUtils
from utilities.log_gen import LogsGen
from utilities.read_prop import ReadConfig


class TestLoginDDT:
    baseurl = ReadConfig.get_url()
    path = "../testData/login_data.xlsx"
    logger = LogsGen.logs()

    def test_ddt_001_login(self, setup):
        self.logger.info("Starting test_ddt_001_login")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        assert "Your store. Login" in act_title

        self.driver.save_screenshot("../Screenshots/login_page.png")
        self.logger.info("Successfully get into login page")
        self.lp = pageObjects.login_page.Login(self.driver)
        self.rows = XLUtils.get_row_count(self.path, "Sheet1")
        self.logger.info(f"Number of row: {self.rows}")

        list_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.read_data(self.path, "Sheet1", r, 1)
            self.password = XLUtils.read_data(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.read_data(self.path, "Sheet1", r, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            self.driver.save_screenshot('../Screenshots/dashboard.png')
            self.logger.info("Successfully get into dashboard page")

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("Passed")
                    self.lp.click_logout()
                    self.logger.info("Login Success")
                elif self.exp == "Fail":
                    self.logger.info("Failed")
                    list_status.append("Fail")
                    self.lp.click_logout()

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("Failed")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("Passed")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("test_ddt_001_login passed")
            assert True
        else:
            self.logger.info("test_ddt_001_login failed")
            assert False

        self.logger.info("End test_001_login")


if __name__ == "__main__":
    TestLoginDDT()
