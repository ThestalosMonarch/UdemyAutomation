# login_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.NAME, "submit")
        self.login_indicator = (By.CSS_SELECTOR, ".ud-btn.ud-btn-medium.ud-btn-secondary.ud-heading-sm[data-purpose='header-login']")
    def check_login(self):
        try:
            # Check if the login indicator is present
            self.driver.find_element(*self.login_indicator).click()
            return False  # Login indicator found, user is not logged in
        except:
            return True  
    def login(self, username, password):
        if not self.check_login():
            self.driver.find_element(*self.username_input).send_keys(username)
            self.driver.find_element(*self.password_input).send_keys(password)
            self.driver.find_element(*self.login_button).click()
                