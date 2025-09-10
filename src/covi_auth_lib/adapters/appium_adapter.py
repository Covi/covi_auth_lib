from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from covi_auth_lib.protocols.ui_interaction_protocol import UIInteractionProtocol

class AppiumAdapter(UIInteractionProtocol):
    """Implementa el protocolo de interacción usando Appium."""

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver

    def fill_field(self, selector: str, value: str) -> None:
        # Asumimos que el selector para Appium es el 'accessibility_id'
        field = self._driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selector)
        field.send_keys(value)

    def click_button(self, selector: str) -> None:
        button = self._driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selector)
        button.click()