from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options= chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # driver.refresh()
# data=driver.find_elements(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]')
# all_portal=driver.find_element(By.LINK_TEXT,"Content portals")
# all_portal.click()

driver.get("https://secure-retreat-92358.herokuapp.com/")
f_name=driver.find_element(By.NAME,"fName")
f_name.send_keys("uday")

l_name=driver.find_element(By.NAME,"lName")
l_name.send_keys("surya")

email=driver.find_element(By.NAME,"email")
email.send_keys("udaysurya@gmail.com")

# submit=driver.find_element(By.LINK_TEXT,"Sign Up")
submit=driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()

# driver.quit()
