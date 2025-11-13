import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("UI Тесты")
@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_navigate_to_forgot_password(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.click_forgot_password_link()

        assert "forgot-password" in browser.current_url

    @allure.title("Ввод email и отправка формы восстановления")
    def test_forgot_password_form_submission(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.click_forgot_password_link()
        login_page.enter_email_for_reset("test@example.com")
        login_page.click_restore_button()
        main_page.wait_for_url_to_contain("/reset-password")
        assert "/reset-password" in browser.current_url

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_toggle_password_visibility_highlights_input(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.click_forgot_password_link()
        login_page.enter_email_for_reset("test@example.com")
        login_page.click_restore_button()
        login_page.wait_for_url_to_contain("/reset-password")

        assert not login_page.is_password_input_active()

        login_page.click_toggle_password_visibility()

        assert login_page.is_password_input_active()
