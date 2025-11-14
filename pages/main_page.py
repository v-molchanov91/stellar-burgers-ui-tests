# import random
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.constructor_page_locators import ConstructorPageLocators


class MainPage(BasePage):

    @allure.step("Клик по ингредиенту '{name}'")
    def click_ingredient(self, name):
        self.click(ConstructorPageLocators.INGREDIENT(name))

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        if self.is_visible(ConstructorPageLocators.DETAILS_INGREDIENT):
            self.click(ConstructorPageLocators.EXIT_DETAILS_INGREDIENT)
            self.wait_until_not_visible(ConstructorPageLocators.DETAILS_INGREDIENT)

    @allure.step("Перейти в Личный кабинет")
    def go_to_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в Ленту заказов")
    def go_to_order_feed(self):
        self.click(MainPageLocators.LENTA_ORDER_BUTTON)
        self.wait_for_url_to_contain("/feed")

    @allure.step("Нажать кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.OPEN_ACCOUNT_BUTTON)

    @allure.step("Получение информации об ингредиенте")
    def is_ingredient_modal_open(self):
        return self.is_visible(ConstructorPageLocators.DETAILS_INGREDIENT)

    @allure.step("Получение номера заказа")
    def place_order(self):
        self.click(MainPageLocators.BUTTON_ORDER)
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_LOADER)
        self.wait_for_visibility(MainPageLocators.MODAL_ORDER_SUCCESS)
        order_num = self.get_text(MainPageLocators.MODAL_ORDER_NUMBER)
        self.click(MainPageLocators.EXIT_ORDER_BUTTON)
        self.wait_for_invisibility(MainPageLocators.MODAL_ORDER_NUMBER)
        return order_num.strip()
