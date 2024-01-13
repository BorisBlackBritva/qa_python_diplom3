import allure
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from helpers.constants import Constants


class TestResetPassword:

    const = Constants()

    @allure.title('Проверка перехода на страницу восстановления пароля по ссылке на странице логина')
    def test_open_forgot_password_page_via_login_page_link(self):

        login_page = LoginPage(self.driver)
        reset_pass_page = ResetPasswordPage(self.driver)

        login_page.open_login_page()
        login_page.click_reset_password_link()

        assert reset_pass_page.get_elem_text(reset_pass_page.RESET_PASSWORD_FORM_TITLE)

    @allure.title('Проверка подтверждения формы восстановления пароля')
    def test_complete_reset_pass_form(self):

        reset_pass_page = ResetPasswordPage(self.driver)

        reset_pass_page.open_reset_password_page()
        reset_pass_page.enter_email(self.const.EMAIL.get('reset_email'))
        reset_pass_page.click_reset_button()

        assert reset_pass_page.get_elem_text(reset_pass_page.RESET_CODE_INPUT) == 'Введите код из письма'

    @allure.title('Проверка скрытия пароля')
    def test_hide_password(self):

        reset_pass_page = ResetPasswordPage(self.driver)

        reset_pass_page.open_reset_password_page()
        reset_pass_page.enter_email(self.const.EMAIL.get('reset_email'))
        reset_pass_page.click_reset_button()
        reset_pass_page.click_hide_password_button()

        assert reset_pass_page.get_attribute_value(reset_pass_page.PASSWORD_INPUT, 'type') == 'text'
