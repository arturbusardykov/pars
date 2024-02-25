from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from .models import Result

def parse_wikipedia(request, title):
    url = f'https://ru.wikipedia.org/wiki/{title}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_text = soup.find('h1', {'id': 'firstHeading'}).text.strip()

    # Сохранение в базу данных
    result = Result(title=title_text)
    result.save()

    return JsonResponse({'title': title_text, 'saved_to_db': True})