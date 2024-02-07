import allure

from pages.locators.base_page_locators import BasePageLoc
from pages.methods.general_page_methods import GeneralPageFunk
from pages.methods.login_page_methods import LoginPageFunk
from pages.methods.base_page_methods import BasePageFunk
from pages.methods.personal_account_page_methods import PersonalAccountPageFunk


class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет')
    def test_open_personal_account(self, create_and_delete_user):

        general_page = GeneralPageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)
        personal_acc_page = PersonalAccountPageFunk(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()

        assert base_page.get_elem_text(personal_acc_page.PROFILE_BUTTON) == 'Профиль'

    @allure.title('Проверка перехода в историю заказов в личном кабинете')
    def test_open_orders_history_board(self, create_and_delete_user, create_order_for_user):

        general_page = GeneralPageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)
        personal_acc_page = PersonalAccountPageFunk(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()
        personal_acc_page.click_order_history_button()

        assert base_page.get_elem_text(personal_acc_page.FIRST_ORDER) == 'Альфа-сахаридный традиционный-галактический бургер'

    @allure.title('Проверка разлогина')
    def test_exit_personal_account(self, create_and_delete_user):

        general_page = GeneralPageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)
        base_page_funk = BasePageFunk(self.driver)
        base_page_loc = BasePageLoc(self.driver)
        personal_acc_page = PersonalAccountPageFunk(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()
        personal_acc_page.click_exit_user_button()

        assert base_page_funk.get_elem_text(base_page_loc.LOGIN_FORM_TITLE) == 'Вход'
