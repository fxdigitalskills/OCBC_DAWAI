import csv


def main():
    zoo_kl = ["elephant", "tiger", "zebra"]
    with open('./data.csv', 'a', encoding="utf-8") as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(zoo_kl)

    print("Data appended to the file successfully")


if __name__ == "__main__":
    main()