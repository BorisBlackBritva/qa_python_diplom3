from selenium.webdriver.common.by import By


class GeneralPageLoc:

    CONSTRUCTOR_BUTTON = [By.XPATH, '//p[text()="Конструктор"]']
    CONSTRUCTOR_TITLE = [By.XPATH, '//h1[text()="Соберите бургер"]']
    ORDERS_BOARD = [By.XPATH, '//p[text()="Лента Заказов"]']
    ORDERS_BOARD_TITLE = [By.XPATH, '//h1[text()="Лента заказов"]']
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
    ORDER_IN_BOARD = [By.XPATH, '//ul[starts-with(@class, "OrderFeed")]/li//h2']
    CLOSED_ORDER_DETAILS_WINDOW = [By.XPATH, '//section[starts-with(@class, "Modal_modal")][2]']
    OPENED_ORDER_DETAILS_WINDOW = [By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]']
    CLOSE_ORDER_DETAILS_WINDOW_BUTTON = [By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]//button']
    BUNS_INGREDIENTS_BUTTON = [By.XPATH, '//span[text()="Булки"]']
    SAUCE_INGREDIENTS_BUTTON = [By.XPATH, '//span[text()="Соусы"]']
    FILLING_INGREDIENTS_BUTTON = [By.XPATH, '//span[text()="Начинки"]']
    BUN_IN_LIST = [By.XPATH, '//h2[text()="Булки"]/following-sibling::ul/a']
    SAUCE_IN_LIST = [By.XPATH, '//h2[text()="Соусы"]/following-sibling::ul/a']
    FILLING_IN_LIST = [By.XPATH, '//h2[text()="Начинки"]/following-sibling::ul/a']
    BUN_COUNTER = [By.XPATH, '//h2[text()="Булки"]/following-sibling::ul/a//p']
    SAUCE_COUNTER = [By.XPATH, '//h2[text()="Соусы"]/following-sibling::ul/a//p']
    FILLING_COUNTER = [By.XPATH, '//h2[text()="Начинки"]/following-sibling::ul/a//p']
    CONSTRUCTOR_BASKET = [By.XPATH, '//section[starts-with(@class, "BurgerConstructor_basket")]']
    CREATE_ORDER_BUTTON = [By.XPATH, '//button[text()="Оформить заказ"]']
    OPENED_CONFIRM_ORDER_WINDOW = [By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]']
    CREATED_ORDER_NUMBER = [By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]//h2']
    CONFIRM_ORDER_CLOSE_BUTTON = [By.XPATH, '//div[starts-with(@class, "Modal_modal__contentBox")]/following-sibling::button']
    OPENED_INGREDIENT_DETAILS_WINDOW = [By.XPATH, '//section[starts-with(@class, "Modal_modal_opened")]']
    CLOSED_INGREDIENT_DETAILS_WINDOW = [By.XPATH, '//section[starts-with(@class, "Modal_modal")]']
    CLOSE_INGREDIENT_DETAILS_BUTTON = [By.XPATH, '//section[starts-with(@class, "Modal_modal")]//button']
    GENERAL_ORDER_COUNTER = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']
    TODAY_ORDER_COUNTER = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']
    FIRST_COMPLETED_ORDER = [By.XPATH, '//div[starts-with(@class, "OrderFeed_orderStatusBox")]//li']

    def __init__(self, driver):

        self.driver = driver
