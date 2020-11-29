from .BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    TITLE = 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    ELEMENT_ENTER = (By.XPATH, "//*[@data-modal-id='new-log-reg']")
    INPUT_EMAIL = (By.ID, "//*[@placeholder='Электронная почта']")
    INPUT_PASSWD = (By.ID, "//*[@placeholder='Введите пароль']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    HREF_FORGET_PASS = (By.XPATH, "//*[@title='Забыли пароль?']")
    LIST_OF_COURSES = (By.XPATH, "//p[text() = 'Курсы']")
    ABOUT_COMPANY = (By.XPATH, "//p[text() = 'О нас']")
    TEST_COURSES = (By.XPATH, "//*[@title='Тестирование']")
    TRIGGER_PYTHON_QA = (By.XPATH, "/html/body/div[1]/div/header[2]/div/div[2]/div[1]/div[2]/div[6]/a/div")
    TEACHERS = (By.XPATH, "/html/body/div[1]/div/header[2]/div/div[2]/div[5]/div[2]/a[4]")
    PYTHON_QA = (By.XPATH, "//div[1]/div[2]/div[6]/div/a[2]")
    TITLE_TESTING = (By.TAG_NAME, "h1")
    TITLE_TEACHERS = (By.TAG_NAME, "h1")

    def check_testing_course(self):
        self._place_cursor(self.LIST_OF_COURSES[1])
        element = self.driver.find_element(*MainPage.TEST_COURSES)
        assert element.text == u'Тестирование'
        element.click()
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.TITLE_TESTING))

    def go_to_info_about_teachers(self):
        self._place_cursor(self.ABOUT_COMPANY[1])
        element = self.driver.find_element(*MainPage.TEACHERS)
        element.click()
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.TITLE_TEACHERS))

    def check_title(self):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.title_is(self.TITLE))

    def open_registration_form(self):
        self._click_element(self.ELEMENT_ENTER)

    def input_email(self, name):
        self._wait_registration_form(self.HREF_FORGET_PASS)
        self._input(self.INPUT_EMAIL, name)

    def input_pass(self, passwd):
        self._input(self.INPUT_PASSWD, passwd)

    def click_submit_button(self):
        self._click_element(self.SUBMIT_BUTTON)

    def login_user(self, name, passwd):
        self._input(self.INPUT_EMAIL, name)
        self._input(self.INPUT_PASSWD, passwd)
        self.click_submit_button()

    def _wait_registration_form(self, locator):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.element_to_be_clickable(locator))

    def go_to_python_qa(self):
        self._place_cursor(self.LIST_OF_COURSES[1])
        self._place_cursor(self.TRIGGER_PYTHON_QA[1])
        self._place_cursor(self.PYTHON_QA[1])
        self._click_element(self.PYTHON_QA)
