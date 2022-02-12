from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render


from random import choice

import requests

API_URL = "http://localhost:8000/api/"


def index(request):
    response = requests.get(API_URL + "words")

    words = response.json()
    random_word = choice(words)

    context = {"word": random_word}

    return render(request, "core/index.html", context)
