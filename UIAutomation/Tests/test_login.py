# test_login.py
import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        login_page = LoginPage(self.driver)
        self.driver.get("https://www.udemy.com/join/login-popup/")
        login_page.login("your_username", "your_password")
        # Add assertions to verify successful login

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
