#instrucciones para ingresar a la página, completar el login y verificar que el login fue exitoso
#creo una función

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, user="standard_user", password_text="secret_sauce"):
    wait = WebDriverWait(driver, 10)

    usuario = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    usuario.send_keys(user) #con esto envío el texto a la caja de texto del usuario


    #definimos la variable para la contraseña
    password = driver.find_element(By.ID,"password")
    password.send_keys(password_text) #con esto envío el texto a la caja de texto de la contraseña

    #hago click en el boton de login
    password.send_keys(Keys.ENTER) #con esto hago click en el boton de login, es como si presionara enter
