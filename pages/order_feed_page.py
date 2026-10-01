import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Выбрать первый заказ в ленте")
    def click_first_order_in_feed(self):
        first_order = self.wait_for_clickable(OrderFeedPageLocators.FIRST_ORDER_LENTA)
        self.click(first_order)

    @allure.step("Получить счётчик 'Выполнено за всё время'")
    def get_total_completed_count(self):
        element = self.wait_for_element_with_text(
            OrderFeedPageLocators.COMPLETE_ORDER_ALL_TIME, timeout=15
        )
        return int(element.text.strip())

    @allure.step("Получить счётчик 'Выполнено за сегодня'")
    def get_today_completed_count(self):
        element = self.wait_for_element_with_text(
            OrderFeedPageLocators.COMPLETE_ORDER_TODAY, timeout=15
        )
        return int(element.text.strip())

    @allure.step("Проверить наличие заказа '{order_number}' в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        return self.is_visible(
            OrderFeedPageLocators.ORDER_IN_PROGRESS(order_number), timeout=15
        )

    @allure.step("Проверить открытие модального окна заказа")
    def is_order_modal_open(self):
        return self.is_visible(OrderFeedPageLocators.MODAL_WINDOW_ORDER)

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_order_feed_loaded(self, timeout=15):
        self.wait_for_visibility(OrderFeedPageLocators.COMPLETE_ORDER_ALL_TIME, timeout)
        self.wait_for_visibility(OrderFeedPageLocators.COMPLETE_ORDER_TODAY, timeout)
