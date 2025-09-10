from covi_auth_lib.protocols.authentication_provider import AuthenticationProvider
from covi_auth_lib.protocols.ui_interaction_protocol import UIInteractionProtocol

class WebAuthenticationProvider(AuthenticationProvider):
    """
    Estrategia de autenticación que interactúa con una UI a través de un adaptador.
    Es agnóstica al framework subyacente (Playwright, Appium, etc.).
    """
    def __init__(
        self,
        ui_adapter: UIInteractionProtocol,
        user_selector: str,
        password_selector: str,
        submit_selector: str,
    ):
        self._adapter = ui_adapter
        self._user_selector = user_selector
        self._password_selector = password_selector
        self._submit_selector = submit_selector

    def authenticate(self, **credentials: str) -> bool:
        """
        Rellena usuario/contraseña y hace clic en 'enviar' usando el adaptador.
        Espera 'user' y 'password' en el diccionario de credenciales.
        """
        try:
            user = credentials['user']
            password = credentials['password']
            
            self._adapter.fill_field(self._user_selector, user)
            self._adapter.fill_field(self._password_selector, password)
            self._adapter.click_button(self._submit_selector)
            return True
        except KeyError as e:
            print(f"Error: Faltan credenciales requeridas ({e})")
            return False
        except Exception as e:
            print(f"Error durante la autenticación web: {e}")
            return False