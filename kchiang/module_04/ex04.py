import os
import requests
from dotenv import load_dotenv

load_dotenv()


NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

URL = "https://newsapi.org/v2/top-headlines"
# URL = "https://newsapi.org/v2/everything"
PARAMS = {
    # "q": "Malaysia OR Selangor OR Kuala Lumpur OR Perak OR Penang OR Johor OR Perlis OR Kedah OR Kelantan OR Terengganu OR Pahang OR Sabah OR Sarawak OR Labuan OR Putrajaya OR Cyberjaya",
    "country": "us",
    # "domains": "paultan.org, thesun.my, thestar.com.my, malaymail.com, freemalaysiatoday.com, themalaysianreserve.com, malaysiakini.com, nst.com.my, bfm.my, sinchew.com.my, chinapress.com.my",
    "pageSize": 20,
    "apiKey": NEWSAPI_KEY,
}


def main():
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
    # print("Top 10 News Articles about Malaysia:")
    print("Top 10 News Articles about the United States:")
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