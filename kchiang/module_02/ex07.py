import csv
import os
from pathlib import Path

CSV_FILE = Path("./vote.csv")


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
    stores: list = []
    with open(CSV_FILE, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile,
            delimiter=',',
            quotechar='\''
        )
        for line in reader:
            line[1] = int(line[1])
            stores.append(line)

    print("Vote for your favourite restaurant:\n")
    n: int = 1
    for store in stores:
        print(f"{n}. {store[0]} - {store[1]} votes")
        n += 1
    print()

    vote: int = 0
    while True:
        vote = input("Enter your vote (enter a number): ")
        if vote.isdigit():
            vote = int(vote)
            if (vote > 0 and vote < n):
                break

    with open(CSV_FILE, 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(
            csvfile,
            delimiter=',',
            quotechar='\'',
            quoting=csv.QUOTE_MINIMAL
        )
        n = 1
        for store in stores:
            if n == vote:
                store[1] += 1
            n += 1
            writer.writerow(store)
    print("\nVote recorded successfully!")
            

if __name__ == "__main__":
    main()