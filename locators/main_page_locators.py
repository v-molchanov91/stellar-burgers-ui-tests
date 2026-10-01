from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')
    OPEN_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]')
    LENTA_ORDER_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]')
    BUTTON_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')
    EXIT_ORDER_BUTTON = (
        By.XPATH,
        ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']/following-sibling::button",
    )
    MODAL_ORDER_NUMBER = (
        By.XPATH,
        ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']",
    )
    MODAL_ORDER_SUCCESS = (By.XPATH, ".//p[text()='идентификатор заказа']")
    MODAL_LOADER = (
        By.XPATH,
        ".//div[contains(@class, 'Modal_modal__container') and .//img[@alt='loading animation']]",
    )
