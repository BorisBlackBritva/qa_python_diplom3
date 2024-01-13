import random
import string
import pytest
import requests
from selenium import webdriver


@pytest.fixture(scope="class", autouse=True)
def fox_driver(request):

    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield driver

    driver.quit()

@pytest.fixture
def create_and_delete_user(request):

    def generate_random_user_credentials():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        email = f'{generate_random_string(10)}@{generate_random_string(10)}.com'
        password = generate_random_string(10)
        name = generate_random_string(10)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload

    payload = generate_random_user_credentials()

    response_1 = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register',
                             json=payload)
    request.cls.user_credentials = payload

    payload['accessToken'] = response_1.json().get('accessToken')

    yield payload

    response_2 = requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user',
                               headers={
                                   'authorization': response_1.json().get('accessToken')
                               }
                               )

@pytest.fixture
def create_order_for_user(create_and_delete_user):

    payload = {"ingredients": ["61c0c5a71d1f82001bdaaa78", "61c0c5a71d1f82001bdaaa74"]}

    requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                         headers={
                             'authorization': create_and_delete_user['accessToken']
                         },
                         json=payload)
