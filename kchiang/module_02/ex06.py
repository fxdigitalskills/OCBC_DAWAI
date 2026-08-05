import csv
from pathlib import Path

CSV_FILE = Path("./ratings.csv")

def main():
    with open(CSV_FILE, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile,
            delimiter=',',
            quotechar='\''
        )
        store   : str = None
        max     : int = 0
        for line in reader:
            line[1] = int(line[1])
            if (line[1] > max):
                store = line[0]
                max = line[1]

    print(f"The most voted restaurant is: {store} with {max} votes!")

if __name__ == "__main__":
    main()