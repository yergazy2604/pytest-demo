
from pages.base_page import BasePage
from utilities.locators import ChangePasswordLocatorsFields
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChangePasswordPage(BasePage):
    
    def __init__(self, driver):        
        self.locate = ChangePasswordLocatorsFields()
        super().__init__(driver)

    def change_password(self, password, confirm_password):
        self.set(self.locate.password_field, password)
        self.set(self.locate.confirm_password_field, confirm_password)
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)
    
    def get_confirmation_error_message(self):
        # Явное ожидание появления текста
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locate.error_message)
        )
        return self.get_text(self.locate.error_message)