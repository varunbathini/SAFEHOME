from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo4.msampleqa.in/login")
driver.find_element(By.XPATH, "//*[@formcontrolname='userId']").send_keys("1")
driver.find_element(By.XPATH, "//*[@type='password']").send_keys("Admin@123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='mat-expansion-panel-header-4']/span[1]/mat-panel-title/div/span").click()
time.sleep(10)
driver.find_element(By.XPATH,"//div[@class='child-name'][normalize-space()='Alerts']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//button[contains(text(),'Create Alert')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//select[@formcontrolname='emergencyTypeId']/option[@value='1']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//textarea[@placeholder='Enter Description']").send_keys("Fire")
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='dropdown-btn']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//ul[@class='item1']//li[@class='multiselect-item-checkbox ng-star-inserted']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
time.sleep(15)
if driver.current_url == "http://demo4.msampleqa.in/auth/alerts":
    print("Alert Added Successfully")
else:
    print("Failed to add an alert")

driver.quit()




