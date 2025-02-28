import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query):
    url = f"https://duckduckgo.com/?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for item in soup.find_all('a', class_='result__a'):
        title = item.get_text()
        link = item['href']
        results.append({'title': title, 'link': link})

    return results