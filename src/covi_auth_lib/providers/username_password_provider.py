from covi_auth_lib.protocols.authentication_provider import AuthenticationProvider
from covi_auth_lib.protocols.ui_interaction_protocol import UIInteractionProtocol

class UsernamePasswordProvider(AuthenticationProvider):
    """
    Estrategia de autenticación para un flujo web clásico de usuario y contraseña.
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
        Provee el usuario/contraseña y desencadena la acción de login.
        Espera 'user' y 'password' en el diccionario de credenciales.
        """
        try:
            user = credentials['user']
            password = credentials['password']
            
            # Órdenes agnósticas, basadas en la intención
            self._adapter.set_value(self._user_selector, user)
            self._adapter.set_value(self._password_selector, password)
            self._adapter.trigger_action(self._submit_selector)
            
            return True
        except KeyError as e:
            print(f"Error: Faltan credenciales requeridas ({e})")
            return False
        except Exception as e:
            print(f"Error durante la autenticación: {e}")
            return False