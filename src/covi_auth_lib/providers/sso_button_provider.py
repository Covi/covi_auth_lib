from covi_auth_lib.protocols.authentication_provider import AuthenticationProvider
from covi_auth_lib.protocols.ui_interaction_protocol import UIInteractionProtocol

class SsoButtonProvider(AuthenticationProvider):
    """
    Estrategia de autenticación para un flujo web que solo requiere
    hacer clic en un único botón (ej. "Login with SSO").
    """
    def __init__(self, ui_adapter: UIInteractionProtocol, sso_button_selector: str):
        self._adapter = ui_adapter
        self._sso_button_selector = sso_button_selector

    def authenticate(self, **credentials) -> bool:
        """
        Hace clic en el botón de SSO. Ignora cualquier credencial pasada.
        """
        try:
            self._adapter.trigger_action(self._sso_button_selector)
            return True
        except Exception as e:
            print(f"Error durante la autenticación SSO: {e}")
            return False