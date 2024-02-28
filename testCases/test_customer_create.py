import random
import string

import pytest
from selenium.webdriver.common.by import By

from pageObjects.customer_create import CreateCustomer
from testCases import test_login_page
from utilities.log_gen import LogsGen
from utilities.read_prop import ReadConfig


class TestAddCustomer:
    baseurl = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogsGen.customer_create_logs()
    login = test_login_page.TestLogin()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_002_add_customer(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.login.try_login(setup)
        self.logger.info("************* Test_002_AddCustomer **********")
        self.logger.info("******* Starting Add Customer Test **********")
        self.create = CreateCustomer(setup)
        self.create.click_on_customers_menu()
        self.create.click_on_customers_setion()
        self.create.click_on_addnew()
        self.logger.info("************* Providing customer info **********")
        self.email = random_generator() + "@gmail.com"
        self.create.set_email(self.email)
        self.create.set_password("test_001_add_customer")
        self.create.set_customer_roles("Administrators")
        self.create.set_first_name("Anggit")
        self.create.set_last_name("Demariza")
        self.create.set_gender("Male")
        self.create.set_dob("8/03/1998")  # Format: D / MM / YYYY
        self.create.set_company_name("busyQA")
        self.create.ver_task()
        self.create.choose_newsletter("Your store name")
        self.create.set_manager_of_vendor("Vendor 2")
        self.create.set_comment("This is for testing.........")
        self.create.click_on_save()
        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")
        msg = setup.find_element(By.TAG_NAME, "body").text
        if 'customer has been added successfully.' in msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot('./Screenshots/customer_creation.png')  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    TestAddCustomer()
