from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_HEADER = (By.XPATH, ".//a[text()='Профиль']")
    HISTORY_ORDER = (By.XPATH, ".//a[text()='История заказов']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    ORDER_HISTORY_LIST = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderHistory_profileList')]",
    )

    @staticmethod
    def ORDER_BY_NUMBER(order_number):
        return (By.XPATH, f".//p[text()='#0{order_number}']")
