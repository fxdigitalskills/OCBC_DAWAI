import requests

# url = "https://www.w3schools.com/python/demopage.htm"
url = "https://finance.yahoo.com/quote/%5EGSPC/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://example.com/",
}

def main():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()