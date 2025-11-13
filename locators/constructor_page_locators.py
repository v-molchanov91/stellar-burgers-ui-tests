from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    @staticmethod
    def INGREDIENT(name):
        return (
            By.XPATH,
            f".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']"
            f"//p[text()='{name}']/ancestor::a",
        )

    DETAILS_INGREDIENT = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    BASKET = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    EXIT_DETAILS_INGREDIENT = (
        By.XPATH,
        './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]/following-sibling::button',
    )

    @staticmethod
    def INGREDIENT_COUNTER(name):
        return (
            By.XPATH,
            f"//p[text()='{name}']/preceding-sibling::div[contains(@class, 'counter_counter__ZNLkj')]//p[contains(@class, 'counter_counter__num')]",
        )
