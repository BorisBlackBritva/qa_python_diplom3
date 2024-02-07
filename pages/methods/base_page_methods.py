from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePageFunk:

    def __init__(self, driver):

        self.driver = driver

    def wait(self, condition, locator):
        return WebDriverWait(self.driver, 10).until(condition(locator))

    def click(self, locator):

        self.driver.find_element(*locator).click()

    def get(self, link):

        self.driver.get(link)

    def send_keys(self, locator, key):

        self.find_element(locator).send_keys(key)

    def find_element(self, locator):

        return self.driver.find_element(*locator)

    def get_elem_text(self, locator):

        return self.driver.find_element(*locator).text

    def get_attribute_value(self, locator, attribute_name):

        elem = self.driver.find_element(*locator)
        return elem.get_attribute(attribute_name)

    def send_keys(self, locator, key):
        self.find_element(locator).send_keys(key)
