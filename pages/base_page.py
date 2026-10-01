from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from seletools.actions import drag_and_drop as drag_and_drop_js
from config.app_conf import BASE_URL
from locators.constructor_page_locators import ConstructorPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, path=""):
        self.driver.get(BASE_URL + path)
        self.close_ingredient_modal_if_open()

    def click(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        self.wait_for_clickable(locator).send_keys(text)

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text.strip()

    def wait_for_url_to_contain(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_until_not_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_element_with_text(self, locator, timeout=10):
        element = self.wait_for_visibility(locator, timeout)
        WebDriverWait(self.driver, timeout).until(
            lambda driver: element.text.strip() != ""
        )
        return element

    def wait_for_presence_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_be_absent(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_to_disappear(self, locator, timeout=10):
        try:
            self.wait_for_presence_of_element(locator, timeout=3)
        except:
            pass
        self.wait_for_element_to_be_absent(locator, timeout)

    def get_current_url(self):
        return self.driver.current_url

    def close_ingredient_modal_if_open(self):
        try:
            if self.is_visible(ConstructorPageLocators.DETAILS_INGREDIENT, timeout=3):
                self.click(ConstructorPageLocators.EXIT_DETAILS_INGREDIENT)
                self.wait_until_not_visible(
                    ConstructorPageLocators.DETAILS_INGREDIENT, timeout=5
                )
        except:
            pass

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_for_clickable(source_locator)
        target = self.wait_for_clickable(target_locator)
        drag_and_drop_js(self.driver, source, target)
