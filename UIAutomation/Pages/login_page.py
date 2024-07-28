# login_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def init_(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.NAME, "submit")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
