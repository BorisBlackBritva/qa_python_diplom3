from selenium.webdriver.common.by import By
from pages.base_page_locators import BasePageLoc
from pages.base_page_methods import BasePageFunk


class PersonalAccountPageLoc:

    PERSONAL_ACCOUNT_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    PROFILE_USER_DATA_FORM = [By.XPATH, '//div[@class="Profile_profile__3dzvr"]']
    ORDER_HISTORY_BUTTON = [By.XPATH, '//a[@href="/account/order-history"]']
    ORDERS_BOARD = [By.XPATH, '//div[starts-with(@class, "OrderHistory_orderHistory")]']
    FIRST_ORDER = [By.XPATH, '//div[starts-with(@class, "OrderHistory_orderHistory")]//li//h2']
    EXIT_USER_BUTTON = [By.XPATH, '//button[text()="Выход"]']

    def __init__(self, driver):

        self.driver = driver