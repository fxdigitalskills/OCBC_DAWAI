from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()


def main():
    crypto_name = input("Enter the cryptocurrency: ").strip().lower()
    try:
        response = cg.get_price(ids=crypto_name, vs_currencies='usd')
        if not response:
            print(f"Cryptocurrency '{crypto_name}' not found.")
        else:
            print(f"The current price of {crypto_name} is ${response[crypto_name]['usd']}")

    except Exception as e:
        print(f"CoinGecko API Error: {e}")


if __name__ == "__main__":
    main()