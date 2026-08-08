from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()


def main():
    try:
        response = cg.get_price(ids='bitcoin', vs_currencies='usd')
        print(f"The current price of Bitcoin is ${response['bitcoin']['usd']}")

    except Exception as e:
        print(f"CoinGecko API Error: {e}")


if __name__ == "__main__":
    main()