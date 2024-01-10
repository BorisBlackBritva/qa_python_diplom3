import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class PersonalAccountPage(BasePage):

    PERSONAL_ACCOUNT_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    PROFILE_BUTTON = [By.XPATH, '//a[text()="Профиль"]']
    PROFILE_USER_DATA_FORM = [By.XPATH, '//div[@class="Profile_profile__3dzvr"]']
    ORDER_HISTORY_BUTTON = [By.XPATH, '//a[@href="/account/order-history"]']
    ORDERS_BOARD = [By.XPATH, '//div[starts-with(@class, "OrderHistory_orderHistory")]']
    FIRST_ORDER = [By.XPATH, '//div[starts-with(@class, "OrderHistory_orderHistory")]//li//h2']


    def __init__(self, driver):

        self.driver = driver

    def open_personal_account_page(self):

        self.get(self.PERSONAL_ACCOUNT_URL)
        self.wait(EC.presence_of_element_located, self.PROFILE_BUTTON)

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
