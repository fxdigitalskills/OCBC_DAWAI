import os
import requests
from dotenv import load_dotenv

load_dotenv()


NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

URL = "https://newsapi.org/v2/everything"


def main():
    keyword = input("Enter a keyword: ").strip()
    PARAMS = {
        "q": keyword,
        "pageSize": 20,
        "apiKey": NEWSAPI_KEY,
    }
    try:
        response = requests.get(URL, params=PARAMS)
        data = response.json()
    except Exception as e:
        print(f"Newsapi error: {e}")
        return

    total = data.get("totalResults", 0)
    if total == 0:
        print("No articles found.")
        return

    articles = data.get("articles", [])
    count = 1
    print(f"Top 10 News Articles about {keyword}:")
    for article in articles:
        title = article.get("title", "N/A")
        source = article.get("source", {"name": "N/A"}).get("name", "N/A")
        publishedAt = article.get("publishedAt", "N/A")
        url = article.get("url", "N/A")
        print(f"\n{count}.\t{title}\n\tSource: {source}\n\tPublished At: {publishedAt}\n\tURL: {url}")
        count += 1
        if count > 10:
            break


if __name__ == "__main__":
    main()