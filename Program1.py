from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.cowin.gov.in/")


faq_link = driver.find_element(By.LINK_TEXT, "create FAQ")
partners_link = driver.find_element(By.LINK_TEXT, "partners")


faq_link.click()
partners_link.click()


time.sleep(2)


window_handles = driver.window_handles


main_window = window_handles[0]
faq_window = window_handles[1]
partners_window = window_handles[2]


print("Main Window Handle:", main_window)
print("FAQ Window Handle:", faq_window)
print("Partners Window Handle:", partners_window)


driver.switch_to.window(faq_window)
driver.close()


driver.switch_to.window(partners_window)
driver.close()


driver.switch_to.window(main_window)


driver.quit()