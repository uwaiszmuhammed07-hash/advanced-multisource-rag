import requests
from bs4 import BeautifulSoup

def load_web(url: str):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    return [{
        "text": text,
        "source": url,
        "type": "website"
    }]