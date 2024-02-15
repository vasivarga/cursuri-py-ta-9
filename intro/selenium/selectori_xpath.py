import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://formy-project.herokuapp.com/form")
driver.maximize_window()

# ################ XPATH Relativ

# ################ Relatii parinte-copil #################


# Primul element copil cu tag-ul <input> al unui element parinte oarecare
driver.find_element(By.XPATH, "//input[1]").send_keys("Test")
time.sleep(1)

# al doilea copil cu tag-ul <div> al unui element parinte oarecare
driver.find_element(By.XPATH, "//div[2]")

# Al doilea copil cu tag-ul ORICARE (*) al unui element parinte oarecare, cu clasa 'form-control'
driver.find_element(By.XPATH, "//*[2][@class='form-control']").clear()
time.sleep(1)

# Primul element copil cu tag-ul <input> cu id='last-name' al unui element parinte <div>
driver.find_element(By.XPATH, "//div/input[1][@id='last-name']").send_keys("Test")
time.sleep(1)

# Ultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()]")

# Penultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()-1]")

# Parintele elementului <input> cu id-ul first-name
driver.find_element(By.XPATH, "//input[@id='first-name']/..")

# ################ XPATH-uri cu operatori logici (and, or, |, not) si atribute cu continut specific (contains) #################

# SIMBOLUL | (pipe) - se foloseste intre 2 xpath-uri
# Input cu id='id-inexistent' sau Input cu id='first-name'
# simbolul pipe | semnifica un SAU logic intre 2 xpath-uri
driver.find_element(By.XPATH, "//input[@id='id-inexistent'] | //input[@id='first-name']").send_keys("Test")
time.sleep(1)

# OPERATORUL or - sau logic
# Input cu id='id-inexistent' sau id='last-name'
# "or" este un SAU logic si se foloseste intre 2 atribute sau doua conditii dintr-un xpath
driver.find_element(By.XPATH, "//input[@id='id-inexistent' or @id='last-name']").clear()
time.sleep(1)

# Input al carui id contine cuvantul "first" SAU cuvantul "last"
driver.find_element(By.XPATH, "//input[contains(@id,'first') or contains(@id,'last')]").clear()
time.sleep(1)

# OPERATORUL and - si logic
# "and" este un SI logic si se foloseste intre 2 atribute sau doua conditii dintr-un xpath
# Input al carui id contine "last" SI cuvantul "name"
driver.find_element(By.XPATH, "//input[contains(@id,'last') and contains(@id,'name')]").send_keys("Test")
time.sleep(1)

# OPERATORUL not - negare logica
# "not" este o negare logica si se foloseste intre 2 atribute sau doua conditii dintr-un xpath
# Input al carui atribut type NU este egal cu 'text'
driver.find_element(By.XPATH, "//input[not(@type='text')]").send_keys("Test")
time.sleep(1)

# Chiar daca sunt mai multe elemente care corespund acestui xpath, programul va scrie dar pe primul
driver.find_element(By.XPATH, "//input").send_keys("Andreea")
time.sleep(2)

# driver.find_elements(By.XPATH, "//input")



# EXERCITIU: Vreau sa verific ca nu este niciun element input care e al 3-lea

# Codul de mai jos da eroare pt ca elementul trebuie sa existe ca sa pot sa verific ca este afisat
# assert False == driver.find_element(By.XPATH, "//input[3]").is_displayed()


# Cum verific corect ca un element nu exista?

# driver.find_elements() returneaza o lista goala daca nu gaseste un element
# deci daca avem o lista goala cand cautam ceva => elementul respectiv nu exista
# si scapam fara eroare

lista_elemente = driver.find_elements(By.XPATH, "//input[3]")
lungime_lista = len(lista_elemente)

assert lungime_lista == 0

def is_element_present(by, locator):
    lista = driver.find_elements(by, locator)
    lungime = len(lista)

    return lungime > 0


def is_element_absent(by, locator):
    lista = driver.find_elements(by, locator)
    lungime = len(lista)

    return lungime == 0


assert is_element_absent(By.XPATH, "//input[3]")

assert not is_element_present(By.XPATH, "//input[3]")