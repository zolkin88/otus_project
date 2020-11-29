from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    INPUT_USER_NAME = (By.ID, "input-username")
    INPUT_PASSWD = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    LOGIN_TITLE = (By.CLASS_NAME, "panel-title")

    def input_name(self, name):
        self._input(self.INPUT_USER_NAME, name)

    def input_pass(self, passwd):
        self._input(self.INPUT_PASSWD, passwd)

    def click_submit_button(self):
        self._click_element(self.SUBMIT_BUTTON)

    def login_user(self, name, passwd):
        self._input(self.INPUT_USER_NAME, name)
        self._input(self.INPUT_PASSWD, passwd)
        self.click_submit_button()

    def check_logout(self):
        return self._get_element_text(self.LOGIN_TITLE)

    def is_admin_page(self):
        admin = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.LOGIN_TITLE))
        if admin.text == u'Please enter your login details.':
            return True
        else:
            return False
