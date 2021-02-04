from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "your-email"
ACCOUNT_PASSWORD = "your-password"
PHONE = "your-phone"

chrome_driver_path = "/Users/dorukhanuzun/chrome-driver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=105149290&keywords=python%20developer&location=Ontario%2C%20Canada&sortBy=R")
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()
time.sleep(3)

username = driver.find_element_by_id("username")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(3)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    listing.click()
    time.sleep(3)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(3)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            dismiss_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            dismiss_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex Application, skipped")
            continue
        else:
            submit_button.click()

        time.sleep(3)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue


time.sleep(5)
driver.quit()



