import allure
from pages.methods.general_page_methods import GeneralPageFunk
from pages.methods.login_page_methods import LoginPageFunk
from pages.methods.base_page_methods import BasePageFunk
from pages.methods.personal_account_page_methods import PersonalAccountPageFunk


class TestOrdersDetails:

    @allure.title('Проверка закрытия модального окна деталей заказа')
    def test_open_order_details(self):

        general_page = GeneralPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)

        general_page.open_main_page()
        general_page.click_order_board_button()
        general_page.open_order_details_window()

        assert "opened" in base_page.get_attribute_value(general_page.CLOSED_ORDER_DETAILS_WINDOW, 'class')

    @allure.title('Проверка наличия созданного заказа в истории и на борде')
    def test_synchronization_orders_in_history_board_and_orders_board(self, create_and_delete_user, create_order_for_user):

        general_page = GeneralPageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)
        personal_acc_page = PersonalAccountPageFunk(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.click_personal_account_button()
        personal_acc_page.click_order_history_button()

        users_order_in_history = base_page.get_elem_text(personal_acc_page.FIRST_ORDER)

        general_page.open_main_page()
        general_page.click_order_board_button()

        users_order_in_board = base_page.get_elem_text(general_page.ORDER_IN_BOARD)

        assert users_order_in_history == users_order_in_board

    @allure.title('Проверка работы счетчика всех заказов')
    def test_general_order_counter(self, create_and_delete_user):

        general_page = GeneralPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)

        general_page.open_main_page()
        general_page.click_order_board_button()

        order_counter_before = base_page.get_elem_text(general_page.GENERAL_ORDER_COUNTER)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.create_order()
        general_page.click_order_board_button()

        order_counter_after = base_page.get_elem_text(general_page.GENERAL_ORDER_COUNTER)

        assert int(order_counter_before) < int(order_counter_after)

    @allure.title('Проверка работы счетчика сегодняшних заказов')
    def test_today_order_counter(self, create_and_delete_user):

        general_page = GeneralPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)

        general_page.open_main_page()
        general_page.click_order_board_button()

        order_counter_before = base_page.get_elem_text(general_page.TODAY_ORDER_COUNTER)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.create_order()
        general_page.click_order_board_button()

        order_counter_after = base_page.get_elem_text(general_page.TODAY_ORDER_COUNTER)

        assert int(order_counter_before) < int(order_counter_after)

    @allure.title('Проверка отображения номера созданного заказа в логе выполненных заказов')
    def test_appear_order_number_in_work_orders_log(self, create_and_delete_user):

        general_page = GeneralPageFunk(self.driver)
        base_page = BasePageFunk(self.driver)
        login_page = LoginPageFunk(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        created_order_number = general_page.create_order()
        general_page.close_confirm_order_window()
        general_page.click_order_board_button()
        firs_completed_order = base_page.get_elem_text(general_page.FIRST_COMPLETED_ORDER)

        assert firs_completed_order == f'0{created_order_number}'
