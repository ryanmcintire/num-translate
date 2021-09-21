from django.http import HttpRequest, QueryDict
from django.test.client import RequestFactory
from num2words import num2words

from numapi.number_translation_service import NumberTranslationService
from numapi.response_objects import NumApiResponseData

from unittest.mock import patch, Mock

from django.test import TestCase

from numapi.views import NumberAPI

import math


class NumApiRequestHandlerTests(TestCase):
    status_ok = "ok"
    status_bad = "There was an error."
    status_unknown = "Unknown error."
    good_num = 123
    translated_good_num = num2words(good_num)

    status_field = "status"
    number_field = "num_to_english"
    system_under_test = NumberAPI()

    good_response_data = NumApiResponseData(status_ok, translated_good_num)
    good_response_content = vars(good_response_data)

    error_data = NumApiResponseData(status_bad, None)
    error_content = vars(error_data)

    value_error = ValueError(status_bad)
    unknown_error = RuntimeError("Catastrophic error")

    def setUp(self):
        patcher = patch('numapi.views.NumberTranslationService')
        self.translation_service = patcher.start()

        self.translation_service.handle_error.return_value = self.error_data
        self.translation_service.from_get.return_value = self.good_response_data
        self.translation_service.from_post.return_value = self.good_response_data

        self.addCleanup(patcher.stop)

    def test_get_proper_request_valid_response(self):
        self.assert_valid_good_response(self.system_under_test.get(HttpRequest()))

    def test_get_value_error_valid_response(self):
        self.translation_service.from_get.side_effect = self.value_error
        response = self.system_under_test.get(HttpRequest())
        self.assert_valid_error_response(response, str(self.value_error))

    def test_get_other_error_valid_response(self):
        self.translation_service.from_get.side_effect = self.unknown_error
        response = self.system_under_test.get(HttpRequest())
        self.assert_valid_error_response(response, self.status_unknown)

    def test_post_proper_request_valid_response(self):
        self.assert_valid_good_response(self.system_under_test.post(HttpRequest()))

    def test_post_value_error_valid_response(self):
        self.translation_service.from_post.side_effect = self.value_error
        response = self.system_under_test.post(HttpRequest())
        self.assert_valid_error_response(response, str(self.value_error))

    def test_post_other_error_valid_response(self):
        self.translation_service.from_post.side_effect = self.unknown_error
        response = self.system_under_test.post(HttpRequest())
        self.assert_valid_error_response(response, self.status_unknown)

    def test_http_method_not_allowed_valid_response(self):
        response = self.system_under_test.http_method_not_allowed(HttpRequest())
        self.assert_valid_error_response(response, "Method not supported.")

    def assert_valid_good_response(self, response: NumApiResponseData):
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, self.good_response_content)

    def assert_valid_error_response(self, response: NumApiResponseData, error_msg: str):
        self.assertEqual(response.status_code, 200)
        self.translation_service.handle_error.assert_called_with(error_msg)
        self.assertJSONEqual(response.content, self.error_content)


class NumberTranslationServiceTests(TestCase):
    http_get = NumberTranslationService.HTTP_GET
    http_post = NumberTranslationService.HTTP_POST
    parameter = NumberTranslationService.PARAMETER
    status_ok = NumberTranslationService.STATUS_OK
    status_bad = "Error"
    test_numbers = [1234, -1234, 0, 1.0000000000001, .000001, -1.0001, -.000001]
    test_malformed = ["12ab", "abc", "123-4432", "", "**"]
    base_path = "/num_to_english"

    error_response = NumApiResponseData(status_bad, None)

    request_factory = RequestFactory()

    def test_from_get_valid_request_good_response(self):
        for num in self.test_numbers:
            request = self._get_request(f"?number={num}")
            response = NumberTranslationService.from_get(request)
            self.assertEqual(response, self._good_response(num))

    def test_from_get_too_large_raises_error(self):
        request = self._get_request(f"?number={math.factorial(170)}")
        self.assert_error(NumberTranslationService.from_get, request, ValueError,
                          NumberTranslationService.ERR_NUM_TOO_LARGE)

    def test_from_get_invalid_method_raises_error(self):
        request = self.request_factory.post(f"/{self.base_path}?number=1234")
        self.assert_error(NumberTranslationService.from_get, request, TypeError,
                          NumberTranslationService.ERR_ONLY_GET)

    def test_from_get_valid_request_num_omitted_raises_error(self):
        request = self._get_request("")
        self.assert_error(NumberTranslationService.from_get, request, ValueError,
                          NumberTranslationService.ERR_NO_NUM_PROVIDED)

    def test_from_get_valid_request_num_param_malformed_raises_error(self):
        for mal in self.test_malformed:
            request = self._get_request(f"/number={mal}")
            self.assert_error(NumberTranslationService.from_get, request, ValueError,
                              NumberTranslationService.ERR_IMPROPER_VALUE)

    def test_from_post_valid_request_good_response(self):
        for num in self.test_numbers:
            request = self._get_post(number=num)
            response = NumberTranslationService.from_post(request)
            self.assertEqual(response, self._good_response(num))

    def test_from_post_too_large_raises_error(self):
        request = self._get_post(number=math.factorial(170))
        self.assert_error(NumberTranslationService.from_post, request, ValueError,
                          NumberTranslationService.ERR_NUM_TOO_LARGE)

    def test_from_post_invalid_method_raises_error(self):
        request = self.request_factory.get(f"/{self.base_path}?number=1234")
        self.assert_error(NumberTranslationService.from_post, request, TypeError,
                          NumberTranslationService.ERR_ONLY_POST)

    def test_from_post_num_omitted_raises_error(self):
        request = self._get_post(field="bad", number=1234)
        self.assert_error(NumberTranslationService.from_post, request, ValueError,
                          NumberTranslationService.ERR_NO_NUM_PROVIDED)

    def test_from_post_valid_request_param_malaformed_raises_error(self):
        for mal in self.test_malformed:
            request = self._get_post(number=mal)
            self.assert_error(NumberTranslationService.from_post, request, ValueError,
                              NumberTranslationService.ERR_IMPROPER_VALUE)

    def assert_error(self, func, arg, e, msg):
        with self.assertRaises(e) as ctx:
            func(arg)
            self.assertEqual(str(ctx.exception), msg)

    def assert_error_msg(self, ctx, msg):
        self.assertEqual(str(ctx.exception), msg)

    def _get_request(self, param_str: str):
        return self.request_factory.get(f"{self.base_path}{param_str}")

    def _get_post(self, field="number", number=None):
        data = {f"{field}": number}
        return self.request_factory.post(self.base_path,
                                         content_type='application/json', data=data)

    def _good_response(self, num: float) -> NumApiResponseData:
        return NumApiResponseData(self.status_ok, num2words(num))
