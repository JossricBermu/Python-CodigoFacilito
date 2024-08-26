# Docstring
# __doc__

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es, o no, palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.

    Examples:

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CodigoFacilito')
    False

    >>> sentence = 'Oso'
    >>> palindromo(sentence)
    True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
