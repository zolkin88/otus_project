from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TeachersPage(BasePage):
    TEACHERS_ON_PAGE = (By.CLASS_NAME, 'teachers')
    LAST_TEACHER = (By.XPATH, '/html/body/div[1]/div/div[3]/div/a[269]/div[3]')
    TEACHERS_NAME = (By.CLASS_NAME, 'teacher__name')
    TEACHERS_WORK = (By.CLASS_NAME, 'teacher__work')
    TEACHERS_BIG_WORK = (By.CLASS_NAME, 'big-teacher__work')

    def find_teachers_name_webelement(self):
        WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.LAST_TEACHER))
        elements = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.TEACHERS_ON_PAGE))
        elements = elements.find_elements(*self.TEACHERS_NAME)
        return elements

    def check_teacher_in_list(self, name):
        elements = self.find_teachers_name_webelement()
        names = []
        for el in elements:
            names.append(el.text)
        assert name in names
        return name

    def get_number_of_teachers(self):
        elements = self.find_teachers_name_webelement()
        names = []
        for el in elements:
            names.append(el.text)
        return len(names)

    def choose_teacher(self, number):
        elements = self.find_teachers_name_webelement()
        elements[number].click()
        info = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
            EC.presence_of_element_located(self.TEACHERS_BIG_WORK))
        return info.text
