import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):

    @allure.step("Выбрать первый заказ в ленте")
    def click_first_order_in_feed(self):
        first_order = self.wait_for_clickable(OrderFeedPageLocators.FIRST_ORDER_LENTA)
        self.click(first_order)

    def get_total_completed_count(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                OrderFeedPageLocators.COMPLETE_ORDER_ALL_TIME
            )
        )
        WebDriverWait(self.driver, 10).until(lambda driver: element.text.strip() != "")
        return int(element.text.strip())

    def get_today_completed_count(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(OrderFeedPageLocators.COMPLETE_ORDER_TODAY)
        )
        WebDriverWait(self.driver, 10).until(lambda driver: element.text.strip() != "")
        return int(element.text.strip())

    def is_order_in_progress(self, order_number):
        in_progress_locator = (
            By.XPATH,
            f".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[text()='{order_number}']",
        )
        return self.is_visible(in_progress_locator)

    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_open(self):
        return self.is_visible(OrderFeedPageLocators.MODAL_WINDOW_ORDER)

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_order_feed_loaded(self, timeout=15):
        self.wait_for_visibility(OrderFeedPageLocators.COMPLETE_ORDER_ALL_TIME, timeout)
        self.wait_for_visibility(OrderFeedPageLocators.COMPLETE_ORDER_TODAY, timeout)
