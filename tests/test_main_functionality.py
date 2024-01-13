import allure
from pages.general_page import GeneralPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.personal_account_page import PersonalAccountPage


class TestMainFunctionality:

    @allure.title('Проверка перехода к конструктору')
    def test_open_constructor(self):

        general_page = GeneralPage(self.driver)
        base_page = BasePage(self.driver)

        general_page.open_main_page()
        general_page.click_constructor_button()

        assert base_page.get_elem_text(general_page.CONSTRUCTOR_TITLE) == 'Соберите бургер'

    @allure.title('Проверка перехода к доске заказов')
    def test_open_orders_board(self):

        general_page = GeneralPage(self.driver)
        base_page = BasePage(self.driver)

        general_page.open_main_page()
        general_page.click_order_board_button()

        assert base_page.get_elem_text(general_page.ORDERS_BOARD_TITLE) == 'Лента заказов'

    @allure.title('Проверка открытия модального окна деталей ингредиента')
    def test_open_test_close_ingredients_details(self):

        general_page = GeneralPage(self.driver)
        base_page = BasePage(self.driver)

        general_page.open_main_page()
        general_page.open_ingredients_details_window()

        assert "opened" in base_page.get_attribute_value(general_page.CLOSED_INGREDIENT_DETAILS_WINDOW, 'class')

    @allure.title('Проверка закрытия модального окна деталей ингредиента')
    def test_close_ingredients_details(self):
        general_page = GeneralPage(self.driver)
        base_page = BasePage(self.driver)

        general_page.open_main_page()
        general_page.open_ingredients_details_window()
        general_page.close_ingredients_details_window()

        assert "opened" not in base_page.get_attribute_value(general_page.CLOSED_INGREDIENT_DETAILS_WINDOW, 'class')

    @allure.title('Проверка работы счетчика ингредиентов')
    def test_ingredient_counter(self):

        general_page = GeneralPage(self.driver)
        base_page = BasePage(self.driver)

        general_page.open_main_page()
        general_page.add_bun()

        assert base_page.get_elem_text(general_page.BUN_COUNTER) == '2'

    @allure.title('Проверка создания заказа')
    def test_create_order(self, create_and_delete_user):

        general_page = GeneralPage(self.driver)
        base_page = BasePage(self.driver)
        login_page = LoginPage(self.driver)
        personal_acc_page = PersonalAccountPage(self.driver)

        login_page.login_user(self.user_credentials['email'], self.user_credentials['password'])
        general_page.create_order()
        general_page.click_personal_account_button()
        personal_acc_page.click_order_history_button()

        assert base_page.get_elem_text(personal_acc_page.FIRST_ORDER) == 'Флюоресцентный бургер'
