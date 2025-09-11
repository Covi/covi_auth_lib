# Covi Auth Lib
Una librería de autenticación reutilizable que implementa el patrón de diseño Strategy para permitir diferentes métodos de autenticación de forma desacoplada.

## Instalación
Instala la librería usando pip. Puedes instalar solo las dependencias que necesites.

### Instalar el núcleo de la librería
```bash
pip install git+[https://github.com/Covi/covi_auth_lib.git](https://github.com/Covi/covi_auth_lib.git)
```
### Instalar con soporte para Playwright
```bash
pip install git+[https://github.com/Covi/covi_auth_lib.git#egg=covi_auth_lib](https://github.com/Covi/covi_auth_lib.git#egg=covi_auth_lib)[playwright]
```
### Instalar con soporte para Appium
```bash
pip install git+[https://github.com/Covi/covi_auth_lib.git#egg=covi_auth_lib](https://github.com/Covi/covi_auth_lib.git#egg=covi_auth_lib)[appium]
```
### Instalar todo
```bash
pip install git+[https://github.com/Covi/covi_auth_lib.git#egg=covi_auth_lib](https://github.com/Covi/covi_auth_lib.git#egg=covi_auth_lib)[all]
```

## Uso
El LoginService se desacopla del método de autenticación a través de una Estrategia (Provider) inyectada.

```python
from playwright.sync_api import sync_playwright
from covi_auth_lib import (
    LoginService, 
    PlaywrightAdapter, 
    WebAuthenticationProvider
)

# 1. Configuración del entorno (ej. Playwright)
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://mi.app.com/login")

    # 2. Composición de objetos (Inyección de Dependencias)
    # El LoginService no sabe nada de Playwright
    adapter = PlaywrightAdapter(page)

    web_provider = WebAuthenticationProvider(
        ui_adapter=adapter,
        user_selector="#username",
        password_selector="#password",
        submit_selector="#login-button"
    )

    login_service = LoginService(provider=web_provider)

    # 3. Ejecución
    success = login_service.login(user="mi_usuario", password="mi_password")

    if success:
        print("¡Login exitoso!")
    else:
        print("Login fallido.")
    
    browser.close()
```
