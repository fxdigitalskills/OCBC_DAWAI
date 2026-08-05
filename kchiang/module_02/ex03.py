import csv


def main():
    cities: str = None;
    while not cities:
        cities = input("Enter 3 city names (space separated): ")

    city_list: list = cities.split(' ')
    with open('./cities.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(city_list)

    print("Data saved to cities.csv!")


if __name__ == "__main__":
    main()