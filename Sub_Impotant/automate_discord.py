from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# current no, and pip import selenium

no = 40526
num_of_messages = 1
driver = webdriver.Chrome()
driver.get('https://discord.com/login')

# Write your email and password  

time.sleep(2)
email = driver.find_element("name", "email")
email.send_keys('choureyakshat916@gmail.com')
password = driver.find_element("name", "password")
password.send_keys('AKSHAT   chourey 09_09_2004_aksilikepython:#$12345')
password.send_keys(Keys.RETURN)
time.sleep(8)

# navigate to the desired group
group = driver.find_element(By.XPATH, '//div[@data-dnd-name="Programmers Palace"]')
group.click()
time.sleep(7)

# navigate to the desired channel count-to-100000
channel = driver.find_element(By.XPATH, '//a[@aria-label="count-to-100000 (text channel)"]')
channel.click()
time.sleep(2) 

# send the message repeatedly
text_area = driver.find_element(By.XPATH, "//div[@role='textbox']")
for i in range(num_of_messages):
    no += 1
    text_area.send_keys(no)
    text_area.send_keys(Keys.RETURN)
    time.sleep(1)

driver.close()
