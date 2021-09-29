from collections import Callable

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from numapi.services.log_service import Logger
from numapi.services.number_translation_service import NumberTranslationService
from .decorators import debug
from .response_models import NumApiResponseData


class NumberAPI(View):
    http_method_names = ["get", "post"]
    _logger = Logger().get_logger()

    def _handle_error(func: Callable) -> JsonResponse:
        def run(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except ValueError as e:
                return self._build_response(NumberTranslationService.handle_error(str(e)))
            except Exception as e:
                self._logger.error("Unknown error")
                self._logger.error(e)
                return self._build_response(NumberTranslationService.handle_error("Unknown error."))

        return run

    @debug
    @_handle_error
    def get(self, request, *args, **kwargs) -> JsonResponse:
        return self._build_response(NumberTranslationService.from_get(request))

    @debug
    @_handle_error
    @csrf_exempt
    def post(self, request, *args, **kwargs) -> JsonResponse:
        return self._build_response(NumberTranslationService.from_post(request))

    @debug
    @_handle_error
    def http_method_not_allowed(self, request, *args, **kwargs) -> JsonResponse:
        raise ValueError("Method not supported.")

    @staticmethod
    def _build_response(response_data: NumApiResponseData) -> JsonResponse:
        return JsonResponse(vars(response_data))


class Display(TemplateView):
    template_name = "numapi/index.html"
