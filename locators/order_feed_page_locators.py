from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    HEAD_LENTA_ORDER = (By.XPATH, ".//h1[text()='История заказов']")
    FIRST_ORDER_LENTA = (
        By.XPATH,
        ".//ul[contains(@class, 'OrderFeed_list')]/li[contains(@class, 'OrderHistory_listItem')][1]",
    )
    MODAL_WINDOW_ORDER = (
        By.XPATH,
        ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/p",
    )
    CLOSE_MODAL_WINDOW_ORDER = (
        By.XPATH,
        ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/following-sibling::button",
    )
    COMPLETE_ORDER_ALL_TIME = (
        By.XPATH,
        ".//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    COMPLETE_ORDER_TODAY = (
        By.XPATH,
        ".//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    ORDER_FEED_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]")

    @staticmethod
    def ORDER_IN_PROGRESS(order_number):
        return (
            By.XPATH,
            f".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[text()='{order_number}']",
        )

    @staticmethod
    def ORDER_BY_NUMBER(order_number):
        return (By.XPATH, f".//p[text()='#0{order_number}']")
