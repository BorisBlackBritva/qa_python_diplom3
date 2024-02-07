from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC


class BasePageFunk:

    def __init__(self, driver):

        self.driver = driver

    def wait(self, condition, locator):
        return WebDriverWait(self.driver, 10).until(condition(locator))

    def find_element(self, locator):

        return self.driver.find_element(*locator)

    def get_elem_text(self, locator):

        return self.driver.find_element(*locator).text

    def get_attribute_value(self, locator, attribute_name):

        elem = self.driver.find_element(*locator)
        return elem.get_attribute(attribute_name)

    def hard_click(self, condition_1, locator_1):

        max_attemps = 0
        while max_attemps <= 5:
            try:
                self.wait(condition_1, locator_1).click()
                break
            except ElementClickInterceptedException:
                max_attemps += max_attemps
                continue
