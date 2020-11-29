from .BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CoursesPage(BasePage):
    USER_NAME = (By.XPATH, "//*[@header2-menu__dropdown-text_name='Дмитрий Золкин']")
    MAIN_LESSONS = (By.CLASS_NAME, "lessons__page")
    LESSONS = (By.TAG_NAME, "a")
    PYTHON_QA = (By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div/a[2]/div/div[1]/picture/img")
    CONTAINER = (By.CLASS_NAME, "container__row")
    CONTAINER_HEAD = (By.TAG_NAME, 'p')

    def get_number_of_courses(self):
        elements = self.driver.find_element(*self.MAIN_LESSONS)
        elements = elements.find_elements(*self.LESSONS)
        return len(elements)

    def get_names_of_courses(self):
        elements = self.driver.find_element(*self.MAIN_LESSONS)
        elements = elements.find_elements(*self.LESSONS)
        names = []
        correct_names = []
        for elem in elements:
            names.append(elem.text)
        for elem in names:
            name = elem.split('\n')
            correct_names.append(name[0])
        return correct_names

    # def go_to_python_qa(self):
    #     self._place_cursor()
    #     self._click_element(self.PYTHON_QA)

    def get_nearest_courses_date(self):
        elements = self.driver.find_elements(*self.CONTAINER)
        elements = elements[3].find_elements(*self.CONTAINER_HEAD)
        return elements[7].text
