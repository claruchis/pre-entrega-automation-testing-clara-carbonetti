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
  * Validación de mensaje de error en pantalla

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Instalar dependencias:

<pre> ```bash pip install -r requirements.txt ``` </pre>

3. Ejecutar los tests:

<pre> ```bash python3 -m pytest -v -s ``` </pre>

## 📊 Generación de reporte

Para generar un reporte en HTML:

<pre> ```bash python3 -m pytest --html=report.html xdg-open report.html ``` </pre>


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
