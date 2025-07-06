from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# driver=webdriver.Chrome(options= chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# driver.refresh()
# price_dollar=driver.find_element(By.CLASS_NAME,"a-price-whole")
# price_cents=driver.find_element(By.CLASS_NAME,"a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# driver.quit()

driver=webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org/")
# driver.refresh()
# data=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[1]/div/ul')
event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget ul time")
event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget ul a")

final_dict={n:{"time":event_times[n].text,"name":event_names[n].text}  for n in range(len(event_times))}
print(final_dict)

driver.quit()