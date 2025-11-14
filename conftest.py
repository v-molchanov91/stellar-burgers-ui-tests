import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from api.user_api import UserAPI
from api.user_helpers import generate_unique_user
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser: chrome or firefox"
    )


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser must be chrome or firefox")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def registered_user():
    user = generate_unique_user()
    try:
        UserAPI.register(user)
    except Exception as e:
        pytest.skip(f"Registration failed: {e}")

    yield user

    try:
        UserAPI.delete(user)
    except Exception:
        pass


@pytest.fixture
def main_page(browser):
    page = MainPage(browser)
    page.open()
    return page


@pytest.fixture
def login_page(browser):
    page = LoginPage(browser)
    page.open("/login")
    return page


@pytest.fixture
def constructor_page(browser):
    return ConstructorPage(browser)


@pytest.fixture
def profile_page(browser):
    return ProfilePage(browser)


@pytest.fixture
def order_feed_page(browser):
    return OrderFeedPage(browser)
