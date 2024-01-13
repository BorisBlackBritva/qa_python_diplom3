import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class PersonalAccountPage(BasePage):

    PERSONAL_ACCOUNT_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    PROFILE_USER_DATA_FORM = [By.XPATH, '//div[@class="Profile_profile__3dzvr"]']
    ORDER_HISTORY_BUTTON = [By.XPATH, '//a[@href="/account/order-history"]']
    ORDERS_BOARD = [By.XPATH, '//div[starts-with(@class, "OrderHistory_orderHistory")]']
    FIRST_ORDER = [By.XPATH, '//div[starts-with(@class, "OrderHistory_orderHistory")]//li//h2']
    EXIT_USER_BUTTON = [By.XPATH, '//button[text()="Выход"]']

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Кликаем "Профиль" в личном кабинете')
    def click_account_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.PROFILE_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.PROFILE_USER_DATA_FORM)

    @allure.step('Кликаем "История заказов" в личном кабинете')
    def click_order_history_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.ORDER_HISTORY_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.ORDERS_BOARD)

    @allure.step('Кликаем "Выход" в личном кабинете')
    def click_exit_user_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.EXIT_USER_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.LOGIN_FORM_TITLE)
