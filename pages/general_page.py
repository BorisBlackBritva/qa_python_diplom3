import time

import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class GeneralPage(BasePage):

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

    @allure.step('Открываем главную страницу')
    def open_main_page(self):

        self.get(self.MAIN_PAGE_URL)
        self.wait(EC.visibility_of_element_located, self.BUN_IN_LIST)

    @allure.step('Кликаем по кнопке перехода в личный кабинет')
    def click_personal_account_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.PERSONAL_ACCOUNT_HEADER_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.PROFILE_BUTTON)

    @allure.step('Кликаем по кнопке перехода к конструктору')
    def click_constructor_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.CONSTRUCTOR_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем по кнопке перехода к доске заказов')
    def click_order_board_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.ORDERS_BOARD).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.ORDERS_BOARD_TITLE)

    @allure.step('Открываем модальное окно деталей заказа')
    def open_order_details_window(self):

        self.click(self.ORDER_IN_BOARD)
        self.wait(EC.presence_of_element_located, self.OPENED_ORDER_DETAILS_WINDOW)

    @allure.step('Закрываем модальное окно деталей заказа')
    def close_order_details_window(self):

        self.click(self.CLOSE_ORDER_DETAILS_WINDOW_BUTTON)

    @allure.step('Добавляем булку в заказ')
    def add_bun(self):

        action = ActionChains(self.driver)
        basket = self.find_element(self.CONSTRUCTOR_BASKET)
        bun = self.find_element(self.BUN_IN_LIST)

        action.drag_and_drop(bun, basket).perform()

    @allure.step('Создаем заказ')
    def create_order(self):

        action = ActionChains(self.driver)
        basket = self.find_element(self.CONSTRUCTOR_BASKET)
        bun = self.find_element(self.BUN_IN_LIST)

        action.drag_and_drop(bun, basket).perform()
        self.click(self.CREATE_ORDER_BUTTON)
        self.wait(EC.presence_of_element_located, self.OPENED_CONFIRM_ORDER_WINDOW)
        time.sleep(1)
        order_number = self.get_elem_text(self.CREATED_ORDER_NUMBER)

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.CONFIRM_ORDER_CLOSE_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue

        return order_number

    @allure.step('Открываем модальное окно деталей ингредиента')
    def open_ingredients_details_window(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.BUN_IN_LIST).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.OPENED_INGREDIENT_DETAILS_WINDOW)

    @allure.step('Закрываем модальное окно деталей ингредиента')
    def close_ingredients_details_window(self):

        self.click(self.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Закрываем модальное окно подтверждения заказа')
    def close_confirm_order_window(self):

        self.click(self.CONFIRM_ORDER_CLOSE_BUTTON)
