from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CreateCustomer:
    # Add customer Page
    customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    customers_section_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath = "//a[@class='btn btn-primary']"
    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_first_name_xpath = "//input[@id='FirstName']"
    txt_last_name_xpath = "//input[@id='LastName']"
    rb_male_gender_id = "Gender_Male"
    rb_female_gender_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_name_xpath = "//input[@id='Company']"
    cb_tax_xpath = "//input[@id='IsTaxExempt']"
    lb_newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    list_newsletter_xpath = '//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]'
    list_nl_1 = '//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[1]'
    list_nl_2 = '//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[2]'
    lb_customer_role_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    list_role_adm_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[1]'
    list_role_reg_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    list_role_vendor_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]'
    list_role_fm_xpath = '//*[@id="f7320b0c-cc50-4c32-899b-2d0d78c79e9b"]'
    list_role_guest = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[3]'
    dd_vendor_manager_xpath = "//select[@id='VendorId']"
    txt_comment_xpath = '//*[@id="AdminComment"]'
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customers_menu(self):
        self.driver.find_element(By.XPATH, self.customers_menu_xpath).click()

    def click_on_customers_setion(self):
        self.driver.find_element(By.XPATH, self.customers_section_xpath).click()

    def click_on_addnew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.txt_first_name_xpath).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.txt_last_name_xpath).send_keys(last_name)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rb_male_gender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rb_female_gender_id).click()
        else:
            self.driver.find_element_by_id(self.rb_male_gender_id).click()

    def set_dob(self, dob):
        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)

    def set_company_name(self, comp_name):
        self.driver.find_element(By.XPATH, self.txt_company_name_xpath).send_keys(comp_name)

    def ver_task(self):
        self.driver.find_element(By.XPATH, self.cb_tax_xpath).click()

    def choose_newsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.lb_newsletter_xpath).click()
        if newsletter == "Your store name":
            list_nl = self.driver.find_element(By.XPATH, self.list_nl_1)
        elif newsletter == "Test store 2":
            list_nl = self.driver.find_element(By.XPATH, self.list_nl_2)
        else:
            list_nl = None
        # list_nl.click() alternate if element not supporting click method :
        self.driver.execute_script("arguments[0].click();", list_nl)  # javaricpt

    def set_customer_roles(self, role):
        self.driver.find_element(By.XPATH, self.lb_customer_role_xpath).click()
        if role == "Registered":
            list_role = self.driver.find_element(By.XPATH, self.list_role_reg_xpath)
        elif role == "Administrators":
            list_role = self.driver.find_element(By.XPATH, self.list_role_adm_xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            list_role = self.driver.find_element(By.XPATH, self.list_role_guest)
        elif role == 'Vendors':
            list_role = self.driver.find_element(By.XPATH, self.list_role_vendor_xpath)
        else:
            list_role = self.driver.find_element(By.XPATH, self.list_role_fm_xpath)
        # list_role.click() alternate if element not supporting click method :
        self.driver.execute_script("arguments[0].click();", list_role)  # javaricpt

    def set_manager_of_vendor(self, value):
        dd = Select(self.driver.find_element(By.XPATH, self.dd_vendor_manager_xpath))
        dd.select_by_visible_text(value)

    def set_comment(self, content):
        self.driver.find_element(By.XPATH, self.txt_comment_xpath).send_keys(content)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
