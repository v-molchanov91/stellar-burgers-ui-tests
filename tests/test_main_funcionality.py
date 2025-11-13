import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from config.app_conf import BASE_URL
from pages.constructor_page import ConstructorPage


@allure.epic("UI Тесты")
@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход в Конструктор")
    def test_navigate_to_constructor(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_constructor()
        assert browser.current_url == BASE_URL

    @allure.title("Переход в Ленту заказов")
    def test_navigate_to_order_feed(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_order_feed()
        assert "feed" in browser.current_url

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_opens(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_ingredient("Филе Люминесцентного тетраодонтимформа")
        assert main_page.is_ingredient_modal_open()

    @allure.title("Закрытие модального окна по крестику")
    def test_close_ingredient_modal(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_ingredient("Краторная булка N-200i")
        main_page.close_ingredient_modal()
        assert not main_page.is_ingredient_modal_open()

    @allure.title("Счётчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, browser, constructor_page):
        main_page = MainPage(browser)
        main_page.open()
        ingredient_name = "Соус Spicy-X"

        initial_counter = constructor_page.get_ingredient_counter(ingredient_name)
        constructor_page.add_ingredient_to_basket(ingredient_name)
        new_counter = constructor_page.get_ingredient_counter(ingredient_name)

        assert new_counter > initial_counter

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(
        self, browser, registered_user, constructor_page
    ):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        constructor_page.assemble_burger()

        order_number = main_page.place_order()
        assert order_number.isdigit()
