import random

uppercase_letters = "ABCDEFGHIKJLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=`~\\|[]{};:,<.>/?"

upper, lower, digits, special = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if digits:
    all += numbers
if special:
    all += symbols

length = 20
amount = 1

for x in range(amount):
    password = "".join(random.sample(all,length))
    print("Generated Password:",password)