import allure
from pages.general_page import GeneralPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет')
    def test_open_personal_account(self, create_and_delete_user):

        general_page = GeneralPage(self.driver)
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        personal_acc_page = PersonalAccountPage(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()

        assert base_page.get_elem_text(personal_acc_page.PROFILE_BUTTON) == 'Профиль'

    @allure.title('Проверка перехода в историю заказов в личном кабинете')
    def test_open_orders_history_board(self, create_and_delete_user, create_order_for_user):

        general_page = GeneralPage(self.driver)
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        personal_acc_page = PersonalAccountPage(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()
        personal_acc_page.click_order_history_button()

        assert base_page.get_elem_text(personal_acc_page.FIRST_ORDER) == 'Альфа-сахаридный традиционный-галактический бургер'

    @allure.title('Проверка разлогина')
    def test_exit_personal_account(self, create_and_delete_user):

        general_page = GeneralPage(self.driver)
        login_page = LoginPage(self.driver)
        base_page = BasePage(self.driver)
        personal_acc_page = PersonalAccountPage(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()
        personal_acc_page.click_exit_user_button()

        assert base_page.get_elem_text(base_page.LOGIN_FORM_TITLE) == 'Вход'
