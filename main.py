from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

firefox_web_driver = "/media/kemal/Kemal Data/Python/100DaysOfCode/geckodriver"
options = Options()
options.add_argument('--headless')
browser = webdriver.Firefox(executable_path=firefox_web_driver, options=options)

browser.get("https://r.onliner.by/ak/?rent_type%5B%5D=1_room&rent_type%5B%5D=2_rooms&rent_type%5B%5D=3_rooms&"
            "rent_type%5B%5D=4_rooms&rent_type%5B%5D=5_rooms&rent_type%5B%5D=6_rooms#bounds%5Blb%5D%5Blat%"
            "5D=53.71215197063466&bounds%5Blb%5D%5Blong%5D=27.235107421875004&bounds%5Brt%5D%5Blat%5D=54.083159502703&"
            "bounds%5Brt%5D%5Blong%5D=27.889480590820316")

links = browser.find_elements_by_class_name("classified")
full_data = {}
for el in links:
    i = 0
    full_text = [el.text]
    full_data[full_text[i].split("\n")[2][2:]] = [full_text[i].split("\n")[2][:2], full_text[i].split("\n")[0],
                                                  el.get_attribute("href")]
    i += 1
print(full_data)
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSd_LdHqC0VoeGxKafMo2cPU8TNjYZb_KP7-FmjKF_HWxI_mYw/viewform?usp=sf_link")

for key, value in full_data.items():
    inputs = browser.find_elements_by_class_name("exportInput")
    inputs[0].send_keys(key)
    inputs[1].send_keys(value[0])
    inputs[2].send_keys(value[1])
    inputs[3].send_keys(value[2])

    send_button = browser.find_element_by_class_name("exportButtonContent")
    send_button.click()

    new_form_link = browser.find_element_by_link_text("Адправіць яшчэ адзін адказ")
    new_form_link.click()
    time.sleep(3)

browser.close()

