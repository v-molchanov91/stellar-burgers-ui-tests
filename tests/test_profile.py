import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.epic("UI тесты")
@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в Личный кабинет")
    def test_navigate_to_personal_account(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        main_page.go_to_personal_account()
        assert "/account" in browser.current_url

    @allure.title("Переход в Историю заказов")
    def test_navigate_to_order_history(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        main_page.go_to_personal_account()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_profile_page_loaded()
        profile_page.go_to_order_history()

        assert "/account/order-history" in browser.current_url

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        main_page.go_to_personal_account()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_profile_page_loaded()
        profile_page.click_logout_button()

        login_page.wait_for_url_to_contain("/login")

        assert "/login" in browser.current_url
