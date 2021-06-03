import random
import string

length = 8

# random.sample() does not produce repeating elements
random_loc = random.sample(range(0, length), 2)

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits

strpass = lower + upper + number
password = ""

for x in range(length):
    if x == random_loc[0]:
        password += random.choice(upper)
    elif x == random_loc[1]:
        password += random.choice(number)
    else:
        password += random.choice(strpass)

print(password)
