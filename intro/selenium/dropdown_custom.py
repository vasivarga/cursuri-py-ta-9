import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://primeng.org/dropdown")
time.sleep(2)

dropdown = driver.find_element(By.XPATH, "//p-dropdown[@optionlabel='name']")
# dropdown.click()
# time.sleep(2)
#
# optiune_gasita = dropdown.find_element(By.XPATH, "//span[text()='New York']")
# optiune_gasita.click()
# time.sleep(2)

def is_element_present(by, locator):
    lista = driver.find_elements(by, locator)
    lungime = len(lista)

    return lungime > 0

def select_dropdown_option(dropdown: WebElement, text: str, has_search = False):
    dropdown.click()
    time.sleep(1)

    if has_search:
        input_search = dropdown.find_element(By.XPATH, "//input")
        input_search.send_keys(text)

    locator_dropdown_item = f"//p-dropdownitem[.='{text}']"

    if is_element_present(By.XPATH, locator_dropdown_item):
        optiune_gasita = dropdown.find_element(By.XPATH, locator_dropdown_item)
        optiune_gasita.click()
        time.sleep(1)
    else:
        raise AssertionError(f"Eroare, optiunea cu textul {text} nu exista!")


select_dropdown_option(dropdown, "New York")

# select_dropdown_option(dropdown, "Rome")

# select_dropdown_option(dropdown, "London")

# select_dropdown_option(dropdown, "Vaslui")


dropdown_countries = driver.find_element(By.XPATH, "//p-dropdown[@filterby='name']")

# dropdown_countries.click()
# time.sleep(1)
#
# input_search = dropdown_countries.find_element(By.XPATH, "//input")
#
# input_search.send_keys("China")
#
# optiune_gasita = dropdown_countries.find_element(By.XPATH, "//p-dropdownitem[.='China']")
#
# optiune_gasita.click()
#
# time.sleep(3)
#
# select_dropdown_option(dropdown, "London")

select_dropdown_option(dropdown_countries, "China", True)

select_dropdown_option(dropdown_countries, "China")
