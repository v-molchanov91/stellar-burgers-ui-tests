import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Войти в аккаунт с email: {email}")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.INPUT_EMAIL, email)
        self.send_keys(LoginPageLocators.INPUT_PASSWORD, password)
        self.click(LoginPageLocators.OPEN_BUTTON)
        self.wait_for_url_to_contain("/")

    @allure.step("Открыть страницу восстановления пароля")
    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ввести email для восстановления пароля: {email}")
    def enter_email_for_reset(self, email):
        self.send_keys(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_restore_button(self):
        self.click(LoginPageLocators.RESTORE_BUTTON)

    @allure.step("Переключить видимость пароля")
    def click_toggle_password_visibility(self):
        self.click(LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY)

    @allure.step("Проверить активность поля ввода пароля")
    def is_password_input_active(self):
        password_field = self.driver.find_element(*LoginPageLocators.INPUT_NEW_PASSWORD)
        return password_field.get_attribute("type") == "text"
