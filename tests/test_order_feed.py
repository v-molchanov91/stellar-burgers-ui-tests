import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage


@allure.epic("UI Тесты")
@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик по заказу открывает модальное окно")
    def test_click_order_opens_modal(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_order_feed()

        order_feed_page = OrderFeedPage(browser)
        order_feed_page.click_first_order_in_feed()

        assert order_feed_page.is_order_modal_open()

    @allure.title("Заказы из Истории отображаются в Ленте")
    def test_user_orders_appear_in_order_feed(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        constructor_page = ConstructorPage(browser)
        constructor_page.assemble_burger()
        order_number = main_page.place_order()

        main_page.go_to_personal_account()
        profile_page = ProfilePage(browser)
        profile_page.wait_for_profile_page_loaded()
        profile_page.go_to_order_history()
        profile_page.wait_for_order_history_loaded()

        assert profile_page.is_order(order_number)

        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.wait_for_order_feed_loaded()

        assert profile_page.is_order(order_number)

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается")
    def test_total_completed_counter_increases(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.wait_for_order_feed_loaded()
        initial_total = order_feed_page.get_total_completed_count()

        main_page.go_to_constructor()
        constructor_page = ConstructorPage(browser)
        constructor_page.assemble_burger()
        main_page.place_order()

        main_page.go_to_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        new_total = order_feed_page.get_total_completed_count()
        assert new_total > initial_total

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_completed_counter_increases(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(browser)
        order_feed_page.wait_for_order_feed_loaded()
        initial_today = order_feed_page.get_today_completed_count()

        main_page.go_to_constructor()
        constructor_page = ConstructorPage(browser)
        constructor_page.assemble_burger()
        main_page.place_order()

        main_page.go_to_order_feed()
        order_feed_page.wait_for_order_feed_loaded()
        new_today = order_feed_page.get_today_completed_count()
        assert new_today > initial_today

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, browser, registered_user):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_button()

        login_page = LoginPage(browser)
        login_page.login(registered_user["email"], registered_user["password"])

        constructor_page = ConstructorPage(browser)
        constructor_page.assemble_burger()
        order_number = main_page.place_order()
        main_page.go_to_order_feed()

        order_feed_page = OrderFeedPage(browser)
        order_feed_page.wait_for_order_feed_loaded()

        assert order_feed_page.is_order_in_progress(order_number)
