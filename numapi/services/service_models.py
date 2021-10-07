import re


def _prep_place():
    """
    Helper method which builds up the list of large numbers following the convention proposed by Conway and Guy, up to
    novencentillion.
    """
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
        11: "nonillion"
    }

    units = ["", "un", "duo", "tre", "quattuor", "quinqua", "se", "septe", "octo", "noven"]
    illions = ["dec", "vigint", "trigint", "quadragint", "quinquagint", "sexagint", "septuagint", "octogint",
               "nonagint", "cent"]

    index = len(place)
    for num in [unit + illion + "illion" for illion in illions for unit in units]:
        index += 1
        place[index] = num

    return place


class NumberEnglishTranslator:
    """
    Number translator class responsible for translating a string representation of a number into
    an English translation up to novencentillion.
    """
    place = _prep_place()

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

    def __init__(self, number: str):
        self._number = number
        try:
            self._translation = self._process(number)
        except ValueError:
            raise ValueError("Invalid number string provided.")
        except KeyError:
            raise OverflowError("Number provided has too many digits")

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
            hundred += "-hundred "
        tens = number % 100
        if 10 <= tens < 20:
            return hundred + cls.special_tens[tens]
        else:
            translation = hundred + " " + cls.tens[tens // 10]
            if tens // 10 > 0:
                translation += "-"
            translation += cls.ones[tens % 10]
            return translation

    def _process_ints(self, int_str):
        """Helper method which orchestrates translation of the integer portion of a number."""
        if len(int_str) == 0:
            return ""
        if int(int_str) == 0:
            return "zero"
        grouping = 3  # numbers are treated in groups of three digits (hundred, ten, and one for each unit)
        lead = len(int_str) % 3 # special treatment for the lead group which may have one or two digits.
        remaining_numbers = [int(int_str[i:i + grouping]) for i in range(lead, len(int_str), grouping)]
        # separating each group into a list of number lists.
        grouped_nums = [int(int_str[0:lead])] + remaining_numbers if lead > 0 else remaining_numbers

        translated_number = ""
        # Each group is then translated.
        for index, group in enumerate(grouped_nums):
            small = self._translate_small(group)
            if not small.isspace():
                translated_number += small + " " + self.place[len(grouped_nums) - index]
                if index < len(grouped_nums) - 1:
                    translated_number += ", "

        return translated_number

    def _process_decs(self, dec_str):
        """Helper method which orchestrates translation of the integer portion of a number."""
        if int(dec_str) == 0:
            return ""
        # iterates one-by-one through decimal digits and translates to English.
        return " point " + " ".join([self.decimals[digit] for digit in dec_str.rstrip("0")])

    def _process(self, number: str):
        negative = ""
        if number.startswith("-"):
            negative = "negative "
            number = number[1:]
        num_str_list = str(number).replace(",", "").split(".")
        if len(num_str_list) > 2:
            raise TypeError("Invalid number type - too many decimals.")

        translation = self._process_ints(num_str_list[0])
        if len(num_str_list) > 1:
            translation += self._process_decs(num_str_list[1])

        return re.sub(' +', ' ', negative + translation).strip().rstrip(",")
