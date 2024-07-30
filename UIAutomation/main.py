# main.py
from selenium import webdriver
from Pages.login_page import LoginPage
from Excel.save_to_excel import ExcelActivities

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.udemy.com/join/login-popup/")
    
    # Perform login
    login_page = LoginPage(driver)
    login_page.login("your_username", "your_password")
    
    # Navigate and extract course data
    #course_page = CoursePage(driver)
    #courses = course_page.get_courses()
    data = {'Name': ['John', 'Anna'], 'Age': [28, 24]}
    filename = 'output.xlsx'
    ExcelActivities.save_to_excel(data, filename)
    # Save to Excel
    #save_to_excel(courses, "UdemyCourses.xlsx")
    
    driver.quit()

if __name__ == "__main__":
    main()
