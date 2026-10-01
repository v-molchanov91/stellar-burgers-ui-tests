import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step("Перейти в раздел 'История заказов'")
    def go_to_order_history(self):
        self.click(ProfilePageLocators.HISTORY_ORDER)
        self.wait_for_url_to_contain("/account/order-history")

    @allure.step("Выйти из аккаунта")
    def click_logout_button(self):
        self.click(ProfilePageLocators.EXIT_BUTTON)

    @allure.step("Дождаться загрузки истории заказов")
    def wait_for_order_history_loaded(self, timeout=10):
        self.wait_for_visibility(ProfilePageLocators.ORDER_HISTORY_LIST, timeout)

    @allure.step("Проверить наличие заказа '{order_number}'")
    def is_order(self, order_number):
        return self.is_visible(
            ProfilePageLocators.ORDER_BY_NUMBER(order_number), timeout=15
        )

    @allure.step("Дождаться загрузки страницы профиля")
    def wait_for_profile_page_loaded(self, timeout=15):
        self.wait_for_url_to_contain("/account")
        self.wait_for_visibility(ProfilePageLocators.PROFILE_HEADER, timeout)
