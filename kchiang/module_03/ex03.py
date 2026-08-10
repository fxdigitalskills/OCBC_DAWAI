import requests
from bs4 import BeautifulSoup

# url = "https://www.w3schools.com/python/demopage.htm"
url = "https://finance.yahoo.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://example.com/",
}


def main():
    stock_name = input("Enter the company name: ").strip().capitalize()
    code = input("Enter the stock symbol: ").strip().upper()

    html_content: str = None
    try:
        response = requests.get(f"{url}/quote/{code}", headers=headers)
        if response.status_code == 200:
            html_content = response.text
        else:
            print(f"Request failed with status code: {response.status_code}")
            return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    soup = BeautifulSoup(html_content, "html.parser")
    snp = soup.find("span", attrs={"class": "yf-1n64cj", "data-testid": "qsp-price"})
    if snp:
        print(f"The price of {stock_name} is ${snp.text}")
    else:
        print(f"Could not find {stock_name} price.")


if __name__ == "__main__":
    main()