# QA Automation - Saucedemo

Proyecto de automatización de pruebas realizado durante mi formación en QA Automation.

## 🔧 Tecnologías utilizadas

* Python
* Selenium
* Pytest

## 🧪 Casos de prueba implementados

* ✔ Login válido

  * Usuario estándar
  * Verificación de redirección a inventario

* ❌ Login inválido

  * Usuario bloqueado
  * Validación de mensaje de error

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Instalar dependencias:

pip install -r requirements.txt

3. Ejecutar los tests:

python3 -m pytest -v -s

## 📊 Generación de reporte

Para generar un reporte en HTML:

python3 -m pytest --html=report.html

Para abrir el reporte en Linux:

xdg-open report.html

## 📁 Estructura del proyecto

* `test/` → contiene los casos de prueba
* `utils/` → funciones reutilizables (login)
* `conftest.py` → configuración y fixtures

## 👩‍💻 Sobre este proyecto

Este proyecto forma parte de mi aprendizaje en QA Automation, donde practico:

* Uso de Selenium para automatización web
* Ejecución de tests con Pytest
* Uso de fixtures para setup y teardown
* Implementación de escenarios positivos y negativos
