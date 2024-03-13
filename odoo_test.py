from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://59727441-16-0-all.runbot185.odoo.com/web/login")
USERNAME = "admin"
PASSWORD = "admin"
CLIENTE = "Deco"
PRODUCTO = "Adelanto"



username = driver.find_element(By.ID, "login")
username.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()


driver.get("https://59727441-16-0-all.runbot185.odoo.com/web#cids=1&menu_id=874&action=1279&model=sale.order&view_type=form")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "partner_id")))
partner_input = driver.find_element(By.ID, "partner_id")
partner_input.click()
time.sleep(5)
partner_input.send_keys(CLIENTE)
time.sleep(5)
partner_input.send_keys(Keys.ENTER)

add_line = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a[1]")
add_line.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/div/div[1]/div/div/input")))

product_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/div/div[1]/div/div/input")
time.sleep(5)
product_input.click()
time.sleep(2)
product_input.send_keys(PRODUCTO)
time.sleep(5)
product_input.send_keys(Keys.ENTER)
time.sleep(2)

price = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div/div[2]/table/tbody/tr[1]/td[9]/div/input")
price.clear()
price.send_keys("1000")
price.send_keys(Keys.ENTER)
time.sleep(2)

confirm_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]/button[2]")
confirm_button.click()

time.sleep(20)

driver.quit()
