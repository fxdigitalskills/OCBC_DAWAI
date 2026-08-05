import csv


def main():
    food_list: list = []
    while True:
        food: str = None
        food = input("Enter a food name (type 'done' to finish): ")
        if not food:
            continue
        if food == "done":
            break

        food_list.append(food)

    with open('./food.csv', 'a', encoding="utf-8") as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(food_list)

    print("Wohoo! My food database is complete!")


if __name__ == "__main__":
    main()