from django.core import serializers
from django.http import HttpResponse


from random import choice

import requests

API_URL = "http://localhost:8000/api/"


def index(request):
    response = requests.get(API_URL + "words")

    words = response.json()
    random_word = choice(words)

    print(random_word)
    print(f"{random_word['spanish']}/{random_word['dutch']}")

    return HttpResponse(f"{random_word['category']['name']}: {random_word['spanish']}/{random_word['dutch']}")
