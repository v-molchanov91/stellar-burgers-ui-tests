from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_HEADER = (By.XPATH, ".//a[text()='Профиль']")
    HISTORY_ORDER = (By.XPATH, ".//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    ORDER_HISTORY_LIST = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderHistory_profileList')]",
    )
