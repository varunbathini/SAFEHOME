from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo4.msampleqa.in/login")
driver.find_element(By.XPATH,"//*[@formcontrolname='userId']").send_keys("1")
driver.find_element(By.XPATH,"//*[@type='password']").send_keys("Admin@123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//mat-expansion-panel-header//span[1]//mat-panel-title//div//span").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[normalize-space()='Parking Spaces']").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div/mat-sidenav-container/mat-sidenav-content/app-parking-layout/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[2]/div").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/app-root/app-layout/div/mat-sidenav-container/mat-sidenav-content/app-parking-layout/div[2]/mat-tab-group/div/mat-tab-body[2]/div/app-lot-parking-list/div/div/div/div/app-table/div/div/div[2]/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"//select[@placeholder='Vehicle Type']/option[@value='1']").click()
time.sleep(5)
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
text = "C"
full_text = f"{text} + {timestamp}"
driver.find_element(By.XPATH,"//input[@placeholder='Enter Level']").send_keys(full_text)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter From Lot number']").send_keys("101")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Enter To Lot number']").send_keys("110")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
time.sleep(10)
if driver.current_url=="http://demo4.msampleqa.in/auth/parking":
    print("Add Lot successful")
else:
    print("Add Lot Failed")
driver.quit()
