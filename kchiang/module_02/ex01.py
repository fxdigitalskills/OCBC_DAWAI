import csv


def main():
    zoo_penang = ["cat", "dog", "mouse"]
    with open('./data.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(zoo_penang)

    print("Data written to the file successfully.")


if __name__ == "__main__":
    main()