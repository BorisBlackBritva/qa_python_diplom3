import allure

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

from pages.locators.base_page_locators import BasePageLoc
from pages.methods.base_page_methods import BasePageFunk
from pages.locators.personal_account_page_locators import PersonalAccountPageLoc


class PersonalAccountPageFunk(BasePageFunk, BasePageLoc, PersonalAccountPageLoc):

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Кликаем "Профиль" в личном кабинете')
    def click_account_button(self):

        self.hard_click(EC.element_to_be_clickable, self.PROFILE_BUTTON)
        self.wait(EC.presence_of_element_located, self.PROFILE_USER_DATA_FORM)

    @allure.step('Кликаем "История заказов" в личном кабинете')
    def click_order_history_button(self):

        self.hard_click(EC.element_to_be_clickable, self.ORDER_HISTORY_BUTTON)
        self.wait(EC.presence_of_element_located, self.ORDERS_BOARD)

    @allure.step('Кликаем "Выход" в личном кабинете')
    def click_exit_user_button(self):

        self.hard_click(EC.element_to_be_clickable, self.EXIT_USER_BUTTON)
        self.wait(EC.presence_of_element_located, self.LOGIN_FORM_TITLE)
