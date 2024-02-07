import time
import allure

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.locators.base_page_locators import BasePageLoc
from pages.methods.base_page_methods import BasePageFunk
from pages.locators.general_page_locators import GeneralPageLoc


class GeneralPageFunk(BasePageFunk, BasePageLoc, GeneralPageLoc):

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.driver.get(self.MAIN_PAGE_URL)
        self.wait(EC.visibility_of_element_located, self.BUN_IN_LIST)

    @allure.step('Кликаем по кнопке перехода в личный кабинет')
    def click_personal_account_button(self):

        self.hard_click(EC.element_to_be_clickable, self.PERSONAL_ACCOUNT_HEADER_BUTTON)
        self.wait(EC.presence_of_element_located, self.PROFILE_BUTTON)

    @allure.step('Кликаем по кнопке перехода к конструктору')
    def click_constructor_button(self):

        self.hard_click(EC.element_to_be_clickable, self.CONSTRUCTOR_BUTTON)
        self.wait(EC.presence_of_element_located, self.CONSTRUCTOR_TITLE)

    @allure.step('Кликаем по кнопке перехода к доске заказов')
    def click_order_board_button(self):

        self.hard_click(EC.element_to_be_clickable, self.ORDERS_BOARD)
        self.wait(EC.presence_of_element_located, self.ORDERS_BOARD_TITLE)

    @allure.step('Открываем модальное окно деталей заказа')
    def open_order_details_window(self):

        self.driver.find_element(*self.ORDER_IN_BOARD).click()
        self.wait(EC.presence_of_element_located, self.OPENED_ORDER_DETAILS_WINDOW)

    @allure.step('Закрываем модальное окно деталей заказа')
    def close_order_details_window(self):

        self.driver.find_element(*self.CLOSE_ORDER_DETAILS_WINDOW_BUTTON).click()


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
        self.driver.find_element(*self.CREATE_ORDER_BUTTON).click()
        self.wait(EC.presence_of_element_located, self.OPENED_CONFIRM_ORDER_WINDOW)
        time.sleep(1) #не нашел другого способа
        order_number = self.get_elem_text(self.CREATED_ORDER_NUMBER)

        self.hard_click(EC.element_to_be_clickable, self.CONFIRM_ORDER_CLOSE_BUTTON)

        return order_number

    @allure.step('Открываем модальное окно деталей ингредиента')
    def open_ingredients_details_window(self):

        self.hard_click(EC.element_to_be_clickable, self.BUN_IN_LIST)
        self.wait(EC.presence_of_element_located, self.OPENED_INGREDIENT_DETAILS_WINDOW)

    @allure.step('Закрываем модальное окно деталей ингредиента')
    def close_ingredients_details_window(self):

        self.driver.find_element(*self.CLOSE_INGREDIENT_DETAILS_BUTTON).click()

    @allure.step('Закрываем модальное окно подтверждения заказа')
    def close_confirm_order_window(self):

        self.driver.find_element(*self.CONFIRM_ORDER_CLOSE_BUTTON).click()
