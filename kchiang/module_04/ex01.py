import requests


ZENQUOTE_URL = "https://zenquotes.io/api/quotes/"


def main():
    try:
        response = requests.get(ZENQUOTE_URL)
        response = response.json()[0]
        print(f"\"{response['q']}\" - {response['a']}")

    except Exception as e:
        print(f"Zenquote API Error: {e}")


if __name__ == "__main__":
    main()