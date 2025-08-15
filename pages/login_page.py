from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.my_account_page import MyAccountPage

class LoginPage(BasePage):
    email_address_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.XPATH, "//input[@value='Login']")
    warning_message = (By.CSS_SELECTOR, "#account-login .alert-danger")

    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email_address):
        self.set(self.email_address_field, email_address)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_login(self):
        self.click(self.login_button)
        return MyAccountPage(self.driver)

    def get_warning_message(self):
        return self.get_text(self.warning_message)
    
    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login()
      
    