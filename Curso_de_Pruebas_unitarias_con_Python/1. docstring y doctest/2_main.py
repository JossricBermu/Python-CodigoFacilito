# Docstring
# __doc__


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es o no un palindromo.

    Args:
        sentence: string

    Returns:
        boll
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
