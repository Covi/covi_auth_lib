from typing import Any
from covi_auth_lib.protocols.authentication_provider import AuthenticationProvider

class LoginService:
    """
    Servicio de login que utiliza una estrategia de autenticación inyectada.
    """
    def __init__(self, provider: AuthenticationProvider):
        if not isinstance(provider, AuthenticationProvider):
            raise TypeError("El proveedor debe implementar la interfaz AuthenticationProvider.")
        self._provider = provider

    def login(self, **credentials: Any) -> bool:
        """
        Delega el proceso de login a la estrategia de autenticación configurada.

        :param credentials: Credenciales necesarias para la estrategia actual.
        :return: True si el login es exitoso, False en caso contrario.
        """
        print(f"Iniciando login con la estrategia: {self._provider.__class__.__name__}")
        return self._provider.authenticate(**credentials)