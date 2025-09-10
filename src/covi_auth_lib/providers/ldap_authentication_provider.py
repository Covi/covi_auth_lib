from covi_auth_lib.protocols.authentication_provider import AuthenticationProvider
from typing import Any

class LdapAuthenticationProvider(AuthenticationProvider):
    """
    TEMPLATE: Estrategia de autenticación contra un servidor LDAP.
    
    Esta clase es una plantilla. Para implementarla, necesitarás:
    1. Instalar la librería 'python-ldap'.
    2. Completar la lógica del método 'authenticate'.
    """

    def __init__(self, server_uri: str, bind_dn_template: str):
        self._server_uri = server_uri
        self._bind_dn_template = bind_dn_template

    def authenticate(self, **credentials: Any) -> bool:
        """
        Intenta hacer un 'bind' a un servidor LDAP.
        
        Levanta un NotImplementedError para indicar que esta lógica 
        debe ser implementada por el desarrollador que use esta clase.
        """
        raise NotImplementedError(
            "Para usar LdapAuthenticationProvider, debes instalar 'python-ldap' "
            "e implementar la lógica de autenticación en este método."
        )