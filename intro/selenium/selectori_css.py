import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

# ################ CSS SELECTORS

"""
 simbolul   *         - selecteaza toate elementele
 #idElement           - selecteaza elementul cu id-ul "idElement"
 .button              - selecteaza elementele care au clasa "button" 
 .button.primary      - selecteaza elementele care au atat clasa "button" cat si clasa "primary"
 input                - selecteaza toate elementele de tip input
 div input            - selecteaza toate elementele de tip input care se afla intr-un div
 div > input          - selecteaza toate elementele de tip input unde parintele e un div
 input[class]         - selecteaza elementele de tip input care au atributul class
 input[class='value'] - selecteaza elementele de tip input care au atributul class = 'value'
 input[class~='value']- selecteaza elementele de tip input ale caror atribut class contine clasa 'value' 
 [id|="radio-button"] - selecteaza toate elementele ale caror id este egal cu sau incepe cu radio-button
"""

driver.find_element(By.CSS_SELECTOR, "input.search-box-text").send_keys("laptop")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#small-searchterms").clear()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "[name='q']").send_keys("Asus")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input#small-searchterms[name='q']").clear()

driver.find_element(By.CSS_SELECTOR, "#small-searchterms").send_keys("Camera" + Keys.ENTER)
time.sleep(1)

# Dropdown - elementul HTML pe care "bate" selectorul trebuie sa fie neaparat de tip select
order_by = Select(driver.find_element(By.ID, "products-orderby"))
order_by.select_by_visible_text("Price: High to Low")
time.sleep(3)

order_by.select_by_index(0)
time.sleep(3)

order_by.select_by_value("15")
time.sleep(3)

# Select-uri moderne care nu au tag HTML select (Angular / React / etc)
driver.get("https://material.angular.io/components/select/overview")
time.sleep(3)

# Ne da eroare, deoarece incercam sa punem in constructor la clasa Select un div
# dropdown_1 = Select(driver.find_element(By.CSS_SELECTOR, "div.mat-mdc-form-field-infix"))
# dropdown_1.select_by_visible_text("Pizza")



