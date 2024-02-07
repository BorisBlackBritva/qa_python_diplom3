from selenium.webdriver.common.by import By


class ResetPasswordPageLoc:

    FORGOT_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    RESET_BUTTON = [By.XPATH, '//button[text()="Восстановить"]']
    RESET_PASSWORD_FORM_TITLE = [By.XPATH, '//h2[text()="Восстановление пароля"]']
    PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']
    RESET_CODE_INPUT = [By.XPATH, '//label[text()="Введите код из письма"]']
    HIDE_PASSWORD_BUTTON = [By.XPATH, '//div[@class="input__icon input__icon-action"]']

    def __init__(self, driver):

        self.driver = driver