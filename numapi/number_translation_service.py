import json
from decimal import Decimal, InvalidOperation

from django.http.request import HttpRequest

from .decorators import debug, for_all_methods
from .response_objects import NumApiResponseData
from .utilities import NumberEnglishTranslator


@for_all_methods(debug)
class NumberTranslationService:
    """
    Service to handle business logic of responding to
    num_to_english requests.
    """

    HTTP_GET = "GET"
    HTTP_POST = "POST"
    PARAMETER = "number"
    STATUS_OK = "ok"
    ERR_ONLY_GET = "Invalid method call. Only supports 'get' requests."
    ERR_ONLY_POST = "Invalid method call. Only supports 'post' requests."
    ERR_IMPROPER_VALUE = "Error: Improper value supplied for 'number'."
    ERR_NUM_TOO_LARGE = "Error: Value supplied for 'number' is too large."
    ERR_NO_NUM_PROVIDED = "Error: 'number' value not provided."

    @classmethod
    def from_get(cls, request: HttpRequest) -> NumApiResponseData:
        """
        Returns from a get request to '?number=<number>' with an english translation
        of the number.
        """

        if request.method != cls.HTTP_GET:
            raise TypeError(cls.ERR_ONLY_GET)
        return cls._get_response(request.GET.get(cls.PARAMETER, None))

    @classmethod
    def from_post(cls, request: HttpRequest) -> NumApiResponseData:
        """
        Returns from a post request with json body {'number':<number>}
        with an english translation of the number.
        """
        if request.method != cls.HTTP_POST:
            raise TypeError(cls.ERR_ONLY_POST)
        return cls._get_response(json.loads(request.body).get(cls.PARAMETER))

    @classmethod
    def handle_error(cls, msg: str) -> NumApiResponseData:
        return NumApiResponseData(msg, None)

    @classmethod
    def _get_response(cls, number: any) -> NumApiResponseData:
        translator = cls._build_translator(number)
        return NumApiResponseData(cls.STATUS_OK, translator.get_translation())

    @classmethod
    def _build_translator(cls, value: any) -> NumberEnglishTranslator:
        # first check if any number was provided.
        if value is None or (isinstance(value, str) and value.strip() == ""):
            raise ValueError(cls.ERR_NO_NUM_PROVIDED)
        # then try to build a translator object
        try:
            return NumberEnglishTranslator(Decimal(value))
        # Overflow error thrown if the number is too large.
        except OverflowError:
            raise ValueError(cls.ERR_NUM_TOO_LARGE)
        # Invalid operation thrown if a non-number is provided.
        except InvalidOperation:
            raise ValueError(cls.ERR_IMPROPER_VALUE)
