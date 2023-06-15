from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

LOGIN = ""
PASSWORD = ""


class TestAuthYandex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_process(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")
        self.assertIn("Авторизация", driver.title)
        elem = driver.find_element_by_name("login")
        elem.send_keys(LOGIN)
        driver.implicitly_wait(2)
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        driver.implicitly_wait(2)
        elem = driver.find_element_by_name("passwd")
        elem.send_keys(PASSWORD)
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)
        time.sleep(20)

    def tearDown(self):
        self.driver.close()