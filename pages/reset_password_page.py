import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ResetPasswordPage(BasePage):

    FORGOT_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    RESET_BUTTON = [By.XPATH, '//button[text()="Восстановить"]']
    RESET_PASSWORD_FORM_TITLE = [By.XPATH, '//h2[text()="Восстановление пароля"]']
    PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']
    RESET_CODE_INPUT = [By.XPATH, '//label[text()="Введите код из письма"]']
    HIDE_PASSWORD_BUTTON = [By.XPATH, '//div[@class="input__icon input__icon-action"]']

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Вводим email')
    def enter_email(self, email):

        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step('Открываем страницу восстановления пароля')
    def open_reset_password_page(self):

        self.get(self.FORGOT_PASSWORD_URL)
        self.wait(EC.presence_of_element_located, self.RESET_PASSWORD_FORM_TITLE)

    @allure.step('Кликаем по кнопке восстановления пароля')
    def click_reset_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.RESET_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
        self.wait(EC.presence_of_element_located, self.RESET_CODE_INPUT)

    @allure.step('Кликаем по кнопке скрытия пароля')
    def click_hide_password_button(self):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(EC.element_to_be_clickable, self.HIDE_PASSWORD_BUTTON).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
