from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo4.msampleqa.in/login")

# Login
driver.find_element(By.XPATH, "//*[@formcontrolname='userId']").send_keys("1")
driver.find_element(By.XPATH, "//*[@type='password']").send_keys("Admin@123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

# Wait for navigation
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Announcements')]"))).click()

# Wait for the target element to be clickable
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Notices')]")))

# Scroll into view and click
driver.execute_script("arguments[0].scrollIntoView(true);", element)
element.click()

# Add Notice
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-uxcl mx-2']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Notice')]"))).click()

# Fill form
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//select[@formcontrolname='noticeTypeId']/option[@value='1']"))).click()
driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Description']").send_keys("Community meetings")

# Select dropdown options
driver.find_element(By.XPATH, "//span[@class='dropdown-btn']").click()
driver.find_element(By.XPATH, "//ul[@class='item1']//li[@class='multiselect-item-checkbox ng-star-inserted']").click()
driver.find_element(By.XPATH, "//select[@formcontrolname='noticeForId']/option[@value='1']").click()

# Submit form
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Verify success
WebDriverWait(driver, 15).until(EC.url_to_be("http://demo4.msampleqa.in/auth/notice"))
print("Notice Added Successfully")

# Close browser
driver.quit()
