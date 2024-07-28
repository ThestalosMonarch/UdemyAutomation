# main.py
from selenium import webdriver
from pages.login_page import LoginPage
from pages.course_page import CoursePage
from utils.excel_utils import save_to_excel

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.udemy.com/join/login-popup/")
    
    # Perform login
    login_page = LoginPage(driver)
    login_page.login("your_username", "your_password")
    
    # Navigate and extract course data
    course_page = CoursePage(driver)
    courses = course_page.get_courses()
    
    # Save to Excel
    #save_to_excel(courses, "UdemyCourses.xlsx")
    
    driver.quit()

if __name__ == "__main__":
    main()
