from playwright.sync_api import Page
from covi_auth_lib.protocols.ui_interaction_protocol import UIInteractionProtocol

class PlaywrightAdapter(UIInteractionProtocol):
    """Implementa el protocolo de interacción usando Playwright."""

    def __init__(self, page: Page):
        self._page = page

    def fill_field(self, selector: str, value: str) -> None:
        self._page.fill(selector, value)

    def click_button(self, selector: str) -> None:
        self._page.click(selector)