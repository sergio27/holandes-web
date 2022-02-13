from django.shortcuts import render


from random import choice

import os
import requests

API_URL = os.environ['AWS_API_URL']


def index(request):
    response = requests.get(API_URL + "words")

    words = response.json()
    random_word = choice(words)

    context = {"word": random_word}

    return render(request, "core/index.html", context)
