from abc import ABC, abstractmethod
from typing import Any

class AuthenticationProvider(ABC):
    """Define la interfaz para cualquier proveedor de autenticación."""

    @abstractmethod
    def authenticate(self, **credentials: Any) -> bool:
        """
        Autentica usando las credenciales proporcionadas.

        :param credentials: Argumentos de palabra clave con las credenciales necesarias 
                            (ej. user="test", password="123").
        :return: True si la autenticación es exitosa, False en caso contrario.
        """
        pass