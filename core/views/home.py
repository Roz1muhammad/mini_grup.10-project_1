from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello World")

from methodism.main import METHODISM
from rest_framework.authtoken.models import Token

# Импортируем наш файл с функциями
from . import methods

class AuthAPI(METHODISM):
    file = methods

    token_key = "Bearer"
    auth_headers = "Authorization"
    token_class = Token

    not_auth_methods = ['register']