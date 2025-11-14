from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators
from api.ingredients_api import get_ingredients_by_type
import random
import allure


class ConstructorPage(BasePage):

    @allure.step("Добавить ингредиент '{name}' в корзину")
    def add_ingredient_to_basket(self, name):
        self.drag_and_drop(
            ConstructorPageLocators.INGREDIENT(name),
            ConstructorPageLocators.BASKET,
        )

    @allure.step("Получить счетчик ингредиента '{name}'")
    def get_ingredient_counter(self, name):
        locator = ConstructorPageLocators.INGREDIENT_COUNTER(name)
        return int(self.get_text(locator))

    @allure.step("Добавить случайный ингредиент типа '{ingredient_type}' в корзину")
    def add_random_ingredient_by_type(self, ingredient_type: str):
        self.wait_for_ingredients_loaded()
        names = get_ingredients_by_type(ingredient_type)
        if not names:
            raise ValueError(f"No ingredients found for type: {ingredient_type}")
        selected = random.choice(names)
        self.wait_for_clickable(ConstructorPageLocators.BASKET)
        self.drag_and_drop(
            ConstructorPageLocators.INGREDIENT(selected),
            ConstructorPageLocators.BASKET,
        )
        return selected

    @allure.step("Собрать бургер: булка → соус → начинка")
    def assemble_burger(self):
        bun = self.add_random_ingredient_by_type("bun")
        sauce = self.add_random_ingredient_by_type("sauce")
        filling = self.add_random_ingredient_by_type("main")
        return {"bun": bun, "sauce": sauce, "filling": filling}

    @allure.step("Дождаться загрузки ингредиентов")
    def wait_for_ingredients_loaded(self, timeout=15):
        self.wait_for_visibility(ConstructorPageLocators.FIRST_INGREDIENT, timeout)
