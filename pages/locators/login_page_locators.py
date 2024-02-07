from selenium.webdriver.common.by import By


class LoginPageLoc:

    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'
    FORGOT_PASSWORD_LINK = [By.XPATH, '//a[@href="/forgot-password"]']
    EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']
    LOGIN_BUTTON = [By.XPATH, '//button[text()="Войти"]']

    def __init__(self, driver):

        self.driver = driver
