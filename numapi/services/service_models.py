import copy
from decimal import Decimal

from num2words import num2words


class NumberEnglishTranslator:
    place = {
        1: "",
        2: "thousand",
        3: "million",
        4: "billion",
        5: "trillion",
        6: "quadrillion",
        7: "quintillion",
        8: "sextillion",
        9: "septillion",
        10: "octillion",
        11: "nonillion",
        12: "decillion",
    }
    ones = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    decimals = {str(k): v for k, v in ones.items()}
    decimals["0"] = "zero"

    special_tens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    tens = {
        0: "",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    def __init__(self, number: Decimal = 0):
        self._number = number
        self._translation = num2words(number)

    def get_translation(self) -> str:
        return self._translation

    def __str__(self):
        return f"NumberEnglishTranslator - {self._number} - {self._translation}"

    @classmethod
    def _translate_ones(cls, ones):
        return ones[ones]

    @classmethod
    def _translate_small(cls, number):
        hundred = cls.ones[number // 100]
        if len(hundred) > 0:
            hundred += "-hundred"
        tens = number % 100
        if 10 <= tens < 20:
            return hundred + cls.special_tens[tens]
        else:
            translation = hundred + " " + cls.tens[tens // 10]
            if tens // 10 > 0:
                translation += "-"
            translation += cls.ones[tens % 10]
            return translation

    def process_ints(self, int_str):
        if len(int_str) == 0:
            return ""
        if int(int_str) == 0:
            return "zero"
        grouping = 3
        lead = len(int_str) % 3
        remaining_numbers = [int(int_str[i:i + grouping]) for i in range(lead, len(int_str), grouping)]
        grouped_nums = [int(int_str[0:lead])] + remaining_numbers if lead > 0 else remaining_numbers

        translated_number = ""
        for index, group in enumerate(grouped_nums):
            small = self._translate_small(group)
            if not small.isspace():
                translated_number += small + self.place[len(grouped_nums) - index]
                if index < len(grouped_nums) - 1:
                    translated_number += ", "

        return translated_number

    def process_decs(self, dec_str):
        if int(dec_str) == 0:
            return ""
        return " point " + " ".join([self.decimals[digit] for digit in dec_str.rstrip("0")])

    def process(self, number: str):
        num_str_list = str(number).replace(",","").split(".")
        if len(num_str_list) > 2:
            raise TypeError("Invalid number type - too many decimals.")

        translation = self.process_ints(num_str_list[0])
        if len(num_str_list) > 1:
            translation += self.process_decs(num_str_list[1])
        return translation

        # first coalesce the type

        # determine if positive or negative

        #
