import allure

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC

from pages.locators.base_page_locators import BasePageLoc
from pages.methods.base_page_methods import BasePageFunk
from pages.locators.login_page_locators import LoginPageLoc


class LoginPageFunk(BasePageFunk, BasePageLoc, LoginPageLoc):

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Открываем страницу логина')
    def open_login_page(self):

        self.driver.get(self.LOGIN_PAGE_URL)
        self.wait(EC.presence_of_element_located, self.LOGIN_FORM_TITLE)

    @allure.step('Кликаем по ссылке на страницу восстановления пароля')
    def click_reset_password_link(self):

        self.hard_click(EC.element_to_be_clickable, self.FORGOT_PASSWORD_LINK)
        self.wait(EC.presence_of_element_located, self.FORGOT_PASSWORD_FORM_TITLE)

    @allure.step('Логиним юзера')
    def login_user(self, email, password):

        self.open_login_page()
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

        self.hard_click(EC.element_to_be_clickable, self.LOGIN_BUTTON)
        self.wait(EC.presence_of_element_located, self.CONSTRUCTOR_TITLE)
