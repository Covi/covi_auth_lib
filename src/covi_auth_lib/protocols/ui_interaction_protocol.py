from typing import Protocol

class UIInteractionProtocol(Protocol):
    """Define una forma genérica de interactuar con una UI."""

    def set_value(self, identifier: str, value: str) -> None:
        """
        Establece un valor para un elemento identificado.
        (La implementación podría ser .fill, .send_keys, etc.)
        """
        ...

    def trigger_action(self, identifier: str) -> None:
        """
        Desencadena una acción en un elemento identificado.
        (La implementación podría ser .click, .press('Enter'), etc.)
        """
        ...