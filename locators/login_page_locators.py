from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, ".//input[@name='name']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@type='password']")
    OPEN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    TOGGLE_PASSWORD_VISIBILITY = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    INPUT_NEW_PASSWORD = (By.XPATH, ".//input[@name='Введите новый пароль']")
