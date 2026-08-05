#!/usr/bin/env python3
# TODO: Refer to the objective and sample output and figure out your own code!
# Time to graduate :p
import random

adj = ["Fearless", "Dumb", "Merciful", "Dandy", "Handsome", "Old"]
animal = ["Otter", "Badger", "Womble", "Falcon", "Bat", "Husky"]

name = input("What is your name?\n")
codename = random.choice(adj) + f" {random.choice(animal)}"
num = random.randrange(1,100)
print(f"{name}, your codename is: {codename}\nYour lucky number is: {num}")
