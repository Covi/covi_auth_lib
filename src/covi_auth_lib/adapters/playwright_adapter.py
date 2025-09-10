from playwright.sync_api import Page
from covi_auth_lib.protocols.ui_interaction_protocol import UIInteractionProtocol

class PlaywrightAdapter(UIInteractionProtocol):
    """Implementa el protocolo de interacción usando Playwright."""

    def __init__(self, page: Page):
        self._page = page

    def set_value(self, identifier: str, value: str) -> None:
        self._page.fill(identifier, value)

    def trigger_action(self, identifier: str) -> None:
        self._page.click(identifier)