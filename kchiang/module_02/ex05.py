import csv
from pathlib import Path

CSV_FILE = Path("./food.csv")

def main():
    with open(CSV_FILE, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile,
            delimiter=',',
            quotechar='\''
        )
        line = next(reader)
    for food in line:
        print(food)


if __name__ == "__main__":
    main()