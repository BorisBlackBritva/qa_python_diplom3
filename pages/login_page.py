import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'
    FORGOT_PASSWORD_LINK = [By.XPATH, '//a[@href="/forgot-password"]']
    EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']
    LOGIN_BUTTON = [By.XPATH, '//button[text()="Войти"]']

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Открываем страницу логина')
    def open_login_page(self):

        self.get(self.LOGIN_PAGE_URL)
        self.wait(EC.presence_of_element_located, self.LOGIN_FORM_TITLE)

    @allure.step('Кликаем по ссылке на страницу восстановления пароля')
    def click_reset_password_link(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.FORGOT_PASSWORD_LINK).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.FORGOT_PASSWORD_FORM_TITLE)

    @allure.step('Логиним юзера')
    def login_user(self, email, password):

        self.open_login_page()
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.LOGIN_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.CONSTRUCTOR_TITLE)
