from decimal import Decimal

from num2words import num2words

class NumberEnglishTranslator:
    number: Decimal

    def __init__(self, number: Decimal):
        self.number = number
        self._translation = num2words(number)

    def get_translation(self) -> str:
        return self._translation
