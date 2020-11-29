from page_objects.MainPage import MainPage
from page_objects.CoursesPage import CoursesPage
from page_objects.PythonQaPage import PythonQaPage
from page_objects.TeachersPage import TeachersPage
import allure

all_info = [u'Управляющий партнёр Express42',
            u'Руководитель отдела подготовки экспертов и управления качеством образования']

info_about_course = {"nearest_date": "21 декабря", "format": "Online", "duration": "5 месяцев",
                     "days": "Пн 20:00, Чт 20:00"}


def test_title_on_main_page(browser):
    with allure.step(u'Открываем главную страницу Ozone.ru'):
        main_page = MainPage(browser)
    with allure.step(u'Проверям, что заголовок равен: ' + MainPage.TITLE):
        main_page.check_title()


def test_check_numbers_of_courses(browser):
    main_page = MainPage(browser)
    with allure.step(u'Проверяем, что в списке курсов есть: Тестирование'):
        main_page.check_testing_course()
    with allure.step(u'Проверяем, что на странице курсов по тестированию 12 курсов'):
        courses_page = CoursesPage(browser)
        numbers = courses_page.get_number_of_courses()
        allure.attach('',
                      'Ожидаемый результат: {0}, Полученный результат: {1}'.format(12, numbers),
                      allure.attachment_type.TEXT)
        assert numbers == 12


def test_python_qa_engineer_in_list(browser):
    main_page = MainPage(browser)
    with allure.step(u'Проверяем, что в списке курсов есть: Тестирование'):
        main_page.check_testing_course()
        courses_page = CoursesPage(browser)
    with allure.step(u'Получаем названия всех курсов'):
        names = courses_page.get_names_of_courses()
    with allure.step(u'Проверяем, что в этом списке есть курс "Python QA Engineer"'):
        allure.attach('',
                      'Ожидаемый результат: {0}, Полученный результат: {1}'.format("Python QA Engineer", names),
                      allure.attachment_type.TEXT)
        assert "Python QA Engineer" in names


def test_check_nearest_courses_python_qa_engineer(browser):
    main_page = MainPage(browser)
    with allure.step(u'Переходим в раздел "Python QA"'):
        main_page.go_to_python_qa()
    with allure.step(u'Проверяем ближайшую дату начала занятий'):
        python_qa_page = PythonQaPage(browser)
        allure.attach('',
                      'Ожидаемый результат: {0}, Полученный результат: {1}'.format(info_about_course['nearest_date'],
                                                                                   python_qa_page.get_nearest_course_date()),
                      allure.attachment_type.TEXT)
        assert info_about_course['nearest_date'] == python_qa_page.get_nearest_course_date()


def test_check_format_course_python_qa_engineer(browser):
    main_page = MainPage(browser)
    with allure.step(u'Переходим в раздел "Python QA"'):
        main_page.go_to_python_qa()
    with allure.step(u'Проверяем формат обучения'):
        python_qa_page = PythonQaPage(browser)
        a = python_qa_page.get_format_course_date()
        allure.attach('',
                      'Ожидаемый результат: {0}, Полученный результат: {1}'.format(info_about_course['format'],
                                                                                   python_qa_page.get_format_course_date()),
                      allure.attachment_type.TEXT)
        assert info_about_course['format'] == python_qa_page.get_format_course_date()


def test_check_duration_of_course_python_qa_engineer(browser):
    main_page = MainPage(browser)
    with allure.step(u'Переходим в раздел "Python QA"'):
        main_page.go_to_python_qa()
    with allure.step(u'Проверяем в какие дни проходят курсы'):
        python_qa_page = PythonQaPage(browser)
        allure.attach('',
                      'Ожидаемый результат: {0}, Полученный результат: {1}'.format(info_about_course['duration'],
                                                                                   python_qa_page.get_course_duration()),
                      allure.attachment_type.TEXT)
        assert info_about_course['duration'] == python_qa_page.get_course_duration()


def test_check_days_of_course_python_qa_engineer(browser):
    main_page = MainPage(browser)
    with allure.step(u'Переходим в раздел "Python QA"'):
        main_page.go_to_python_qa()
    with allure.step(u'Проверяем в какие дни проходят курсы'):
        python_qa_page = PythonQaPage(browser)
        allure.attach('',
                      'Ожидаемый результат: {0}, Полученный результат: {1}'.format(info_about_course['days'],
                                                                                   python_qa_page.get_course_days()),
                      allure.attachment_type.TEXT)
        assert info_about_course['days'] == python_qa_page.get_course_days()


def test_number_of_teachers(browser):
    with allure.step(u'Открываем главную страницу OTUS'):
        main_page = MainPage(browser)
    with allure.step(u'Переходим на страницу с именами всех преподавателей'):
        main_page.go_to_info_about_teachers()
        teachers_page = TeachersPage(browser)
    with allure.step(u'Проверяем, количество преподавателй на странице'):
        assert 269 == teachers_page.get_number_of_teachers()
    allure.attach('',
                  'Ожидаемый результат: {0}, Полученный результат: {1}'.format(269,
                                                                               teachers_page.get_number_of_teachers()),
                  allure.attachment_type.TEXT)


def test_check_teacher_name(browser):
    with allure.step(u'Открываем главную страницу OTUS'):
        main_page = MainPage(browser)
    with allure.step(u'Переходим на страницу с именами всех преподавателей'):
        main_page.go_to_info_about_teachers()
        teachers_page = TeachersPage(browser)
    with allure.step(u'Проверяем, что в списке, есть нужный нам преподаватель'):
        teachers_page.check_teacher_in_list(u'Семён Вяземский')


def test_get_all_info_about_teacher(browser):
    with allure.step(u'Открываем главную страницу OTUS'):
        main_page = MainPage(browser)
    with allure.step(u'Переходим на страницу с именами всех преподавателей'):
        main_page.go_to_info_about_teachers()
        teachers_page = TeachersPage(browser)
    with allure.step(u'Выбираем преподавателя по номеру и проверяем его должность'):
        info = teachers_page.choose_teacher(3)
    with allure.step(u'Проверяем, что должность преподавателя присутствует в списке должностей'):
        assert info in all_info
    allure.attach('',
                  'Ожидаемый результат: {0}, Полученный результат: {1}'.format(all_info, info),
                  allure.attachment_type.TEXT)
