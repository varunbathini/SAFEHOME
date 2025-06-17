from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo4.msampleqa.in/login")
driver.find_element(By.XPATH,"//*[@formcontrolname='userId']").send_keys("1")
driver.find_element(By.XPATH,"//*[@type='password']").send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(5)
if driver.current_url== "http://demo4.msampleqa.in/auth/dashboard":
    print("Login Successful")
else:
    print("Login Failed")
driver.quit()

