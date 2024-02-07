import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementClickInterceptedException

from pages.locators.base_page_locators import BasePageLoc
from pages.methods.base_page_methods import BasePageFunk
from pages.locators.reset_password_page_lcoators import ResetPasswordPageLoc


class ResetPasswordPageFunk(BasePageFunk, BasePageLoc, ResetPasswordPageLoc):

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Вводим email')
    def enter_email(self, email):

        self.find_element(self.EMAIL_INPUT).send_keys(email)

    @allure.step('Открываем страницу восстановления пароля')
    def open_reset_password_page(self):

        self.driver.get(self.FORGOT_PASSWORD_URL)
        self.wait(EC.presence_of_element_located, self.RESET_PASSWORD_FORM_TITLE)

    @allure.step('Кликаем по кнопке восстановления пароля')
    def click_reset_button(self):

        self.hard_click(EC.element_to_be_clickable, self.RESET_BUTTON)
        self.wait(EC.presence_of_element_located, self.RESET_CODE_INPUT)

    @allure.step('Кликаем по кнопке скрытия пароля')
    def click_hide_password_button(self):

        self.hard_click(EC.element_to_be_clickable, self.HIDE_PASSWORD_BUTTON)
