from asyncio import wait
from time import sleep,time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/feed/")

# Wait for page to load just in case
sleep(3)

print("Looking for Search bar...")
try:
    email_inputs = driver.find_elements(By.CSS_SELECTOR, "form div input")

    username_input = driver.find_element(By.NAME, "session_key")
    password_input = driver.find_element(By.NAME, "session_password")

    # Send values
    username_input.send_keys("udaysurya1597@gmail.com")
    password_input.send_keys("He@dfones3")
    sign_in_button=driver.find_element(By.CSS_SELECTOR, "form div button")
    sign_in_button.click()
    sleep(2)
    input("click enter once security puzzles are done.")

    search_bar=driver.find_element(By.CSS_SELECTOR, "div header div input")
    search_bar.click()
    search_bar.send_keys("Python developer",Keys.ENTER)
    sleep(2)
    links = driver.find_elements(By.CSS_SELECTOR, "a")

    for link in links:
        text = link.text.strip()
        if "Easy apply" in text:
            link.click()  # or store it for later
            break
    sleep(3)
    container_div = driver.find_element(By.CSS_SELECTOR, "div.CENSNYyjUBqTokbIXTuybRoMlHoEzrBFvw")

    # Step 2: Find the <ul> inside it
    ul = container_div.find_element(By.CSS_SELECTOR, "ul.sPjpgbyxyDBHcovoUDFvkPFkSAMhQIJkP")

    # Step 3: Get all <li> items inside that <ul>
    li_items = ul.find_elements(By.TAG_NAME, "li")

    for idx, li in enumerate(li_items):
        try:
            # Scroll into view and click job card
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", li)
            ActionChains(driver).move_to_element(li).click().perform()
            print(f"🔹 Clicked job card {idx + 1}")
            sleep(2)

            # Click either Save or Saved button if present
            try:
                save_button = driver.find_element(By.XPATH, "//button[span[text()='Save'] or span[text()='Saved']]")
                save_button.click()
                print("✅ Save/Saved button clicked.")
            except NoSuchElementException:
                print("⚠️ No Save/Saved button found.")

            sleep(1)

        except Exception as e:
            print(f"❌ Error at job {idx + 1}: {e}")
            continue
    #
    #
    # for idx, li in enumerate(li_items):
    #     try:
    #         job_title = li.find_element(By.CSS_SELECTOR, "a.job-card-list__title--link").text.strip()
    #     except:
    #         job_title = "N/A"
    #
    #     try:
    #         job_link = li.find_element(By.CSS_SELECTOR, "a.job-card-list__title--link").get_attribute("href")
    #     except:
    #         job_link = "N/A"
    #
    #     try:
    #         company_name = li.find_element(By.CSS_SELECTOR, "div.artdeco-entity-lockup__subtitle").text.strip()
    #     except:
    #         company_name = "N/A"
    #
    #     try:
    #         location = li.find_element(By.CSS_SELECTOR, "ul.job-card-container__metadata-wrapper li").text.strip()
    #     except:
    #         location = "N/A"
    #
    #     try:
    #         logo_url = li.find_element(By.CSS_SELECTOR, "img[alt$='logo']").get_attribute("src")
    #     except:
    #         logo_url = "N/A"
    #
    #     try:
    #         footer_items = li.find_elements(By.CSS_SELECTOR, "ul.job-card-list__footer-wrapper li")
    #         footer_texts = [item.text.strip() for item in footer_items]
    #     except:
    #         footer_texts = []
    #
    #     easy_apply = any("Easy Apply" in text for text in footer_texts)
    #     viewed = "Viewed" in footer_texts
    #     promoted = "Promoted" in footer_texts
    #
    #     try:
    #         connection_info = li.find_element(By.CSS_SELECTOR, "div.job-card-container__job-insight-text").text.strip()
    #     except:
    #         connection_info = "N/A"
    #
    #     try:
    #         job_id = li.get_attribute("data-occludable-job-id")
    #     except:
    #         job_id = "N/A"
    #
    #     print(f"\n----- Job {idx + 1} -----")
    #     print(f"Job Title     : {job_title}")
    #     print(f"Job Link      : {job_link}")
    #     print(f"Company       : {company_name}")
    #     print(f"Location      : {location}")
    #     print(f"Logo URL      : {logo_url}")
    #     print(f"Viewed        : {viewed}")
    #     print(f"Promoted      : {promoted}")
    #     print(f"Easy Apply    : {easy_apply}")
    #     print(f"Connection    : {connection_info}")
    #     print(f"Job ID        : {job_id}")
    #     print(f"Footer Tags   : {footer_texts}")

    # frames = driver.find_elements(*(By.XPATH, '//iframe'))
    # for idx, frame in enumerate(frames):
    #     print(f"\n--- Frame {idx} ---")
    #     print("ID:", frame.get_attribute("id"))
    #     print("Name:", frame.get_attribute("name"))
    #     print("Title:", frame.get_attribute("title"))
    #     print("Src:", frame.get_attribute("src"))
    # driver.switch_to.frame(frames[2])
    # print("Switched to Frame 2")
    # button=driver.find_element(By.CLASS_NAME,"nsm7Bb-HzV7m-LgbsSe-BPrWId")
    # button.click()
    # sleep(3)
    # email_input=driver.find_element(By.CSS_SELECTOR,"input")
    # print(email_input.text)
    # email_input.send_keys("udaysurya1597@gmail.com")
except NoSuchElementException:
    print("Language selection not found")

# driver.quit()

