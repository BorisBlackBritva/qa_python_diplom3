from selenium.webdriver.common.by import By


class BasePageLoc:

    def __init__(self, driver):

        self.driver = driver

    PERSONAL_ACCOUNT_HEADER_BUTTON = [By.XPATH, '//p[text()="Личный Кабинет"]']
    FORGOT_PASSWORD_FORM_TITLE = [By.XPATH, '//h2[text()="Восстановление пароля"]']
    LOGIN_FORM_TITLE = [By.XPATH, '//h2[text()="Вход"]']
    CONSTRUCTOR_TITLE = [By.XPATH, '//h1[text()="Соберите бургер"]']
    PROFILE_BUTTON = [By.XPATH, '//a[text()="Профиль"]']
