#traigo a selenium y al webdriver de chrome, luego abro la pagina y por ultimo cierro el navegador
#by y keys hay que importarlos en cada archivo que los vayamos a usar, son parte de selenium.webdriver.common

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_validation (login_in_driver): #con esto le digo a pytest que este test va a usar el fixture login_in_driver, que a su vez usa el fixture driver

    driver = login_in_driver #con esto asigno el valor del fixture login_in_driver a la variable driver para poder usarla en el test

# creo la espera
    wait = WebDriverWait(driver,10)      

#con esto verifico que la URL actual del navegador contenga "/inventory.html"
    
    assert "/inventory.html" in driver.current_url 

 # espera explícita al título Products
    titulo = wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME,"title")
        )
    )

    # valida texto
    assert titulo.text == "Products"