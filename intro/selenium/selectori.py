import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# pentru varianta aceasta instalam selenium
driver = webdriver.Chrome()

# Alternativa pt browser mai customizat

# pentru varianta aceasta instalam webdriver-manager

# service_chrome = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_chrome)

driver.get("https://demo.nopcommerce.com/")

search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("telefon")

textul_de_pe_searchbox = search_box.get_attribute("value")
print(textul_de_pe_searchbox)
search_box.clear()
search_box.send_keys("telefon")
search_button = driver.find_element(By.CLASS_NAME, "search-box-button")

search_button.click()

driver.back()

# Da eroare StaleElementReferenceException, deoarece elementele s-au distrus cand am navigat de pe pagina
# Va trebui sa gasim din nou elementul
# search_box.send_keys("laptop")
# search_button.click()

# search_box_2 = driver.find_element(By.ID, "small-searchterms").send_keys("laptop")

driver.find_element(By.ID, "small-searchterms").send_keys("laptop")
driver.find_element(By.CLASS_NAME, "search-box-button").click()

lista_produse = driver.find_elements(By.CLASS_NAME, "product-item")

print(len(lista_produse))

for element in lista_produse:
    # cautam element in element:
    element_interior = element.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
    print(element_interior.text)

link_laptop_asus = driver.find_element(By.LINK_TEXT, "Asus N551JK-XO076H Laptop")
# link_laptop_asus.click()

link_text_partial_laptop_asus = driver.find_element(By.PARTIAL_LINK_TEXT, "N551JK-XO076H")
# link_text_partial_laptop_asus.click()

assert link_text_partial_laptop_asus.is_displayed(), "Linkul partial nu este vizibil"

element_inexistent = driver.find_elements(By.ID, "SDFDFGDFGFG")
assert len(element_inexistent) == 0

time.sleep(5)
