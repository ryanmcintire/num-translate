from decimal import Decimal

from num2words import num2words

class NumberEnglishTranslator:
    _number: Decimal

    def __init__(self, number: Decimal):
        self._number = number
        self._translation = num2words(number)

    def get_translation(self) -> str:
        return self._translation

    def __str__(self):
        return f"NumberEnglishTranslator - {self._number} - {self._translation}"
