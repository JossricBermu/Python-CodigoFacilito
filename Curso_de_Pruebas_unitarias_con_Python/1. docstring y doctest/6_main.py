"""Este es el Docstring del módulo main."""

# Docstring
# __doc__

class User:
    """Permite representar un usuario."""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo User.

        Args:
            username (str): El username del usuario
            password (str): El password del usuario
        """

        self.username = username
        self.password = password

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]