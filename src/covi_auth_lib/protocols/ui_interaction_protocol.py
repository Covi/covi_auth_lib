from typing import Protocol

class UIInteractionProtocol(Protocol):
    """Define una forma genérica de interactuar con una UI."""

    def fill_field(self, selector: str, value: str) -> None:
        """Rellena un campo identificado por un selector con un valor."""
        ...

    def click_button(self, selector: str) -> None:
        """Hace clic en un botón identificado por un selector."""
        ...