import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="https://otus.ru")
    parser.addoption("--path", default="/")
    parser.addoption("--selenoid", default="No")


@pytest.fixture
def get_base_url(request):
    base_url = request.config.getoption("--base_url")
    return base_url


@pytest.fixture
def get_path(request):
    path = request.config.getoption("--path")
    return path


@pytest.fixture
def browser(request, get_base_url, get_path):
    if "chrome" == request.config.getoption("--browser"):
        chrome_options = ChromeOptions()
        chrome_options.headless = False
        driver = webdriver.Chrome(executable_path='/var/lib/jenkins/workspace/test_otus/last_work/tests/chromedriver',
                                  options=chrome_options)
        driver.maximize_window()
    if "firefox" == request.config.getoption("--browser"):
        firefox_options = FirefoxOptions()
        firefox_options.headless = True
        driver = webdriver.Firefox(executable_path='/var/lib/jenkins/workspace/test_otus/last_work/tests/geckodriver',
                                   options=firefox_options)
        driver.maximize_window()
    if "firefox" == request.config.getoption("--browser") and "Yes" == request.config.getoption("--selenoid"):
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "82.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=capabilities)

    def open(path=get_path):
        return driver.get(get_base_url + path)

    driver.open = open
    driver.open()
    yield driver
    driver.quit()
