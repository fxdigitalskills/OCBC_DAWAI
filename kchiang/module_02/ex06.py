import csv
from pathlib import Path

CSV_FILE = Path("./ratings.csv")


def file_is_invalid():
    if not CSV_FILE.exists():
        print(f"Error: {CSV_FILE} does not exist.")
        return True
    if not CSV_FILE.is_file():
        print(f"Error: {CSV_FILE} is not a file.")
        return True
    if os.access(CSV_FILE, os.R_OK) is False:
        print(f"Error: {CSV_FILE} is not readable.")
        return True
    return False


def main():
    if file_is_invalid():
        return
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
