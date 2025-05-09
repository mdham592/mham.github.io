# Mason Ham
# Basic Password Strength checker
# SDK Python 3.8

import math
import string

# If you use Lowercase, Uppercase, Numbers, Shift + [0-9] Symbols, and Other Symbols. If all character types are used, the range can reach 95.
lc = 26
uc = 26
num = 10
sym = 10
oSym = 13
range = 0
entropy = 0


# Method to check password against known exposed password lists
def password_exposed_check(password):
    exposed = False
    with open(r'D:\projects\10k-common-passwords.txt', 'r') as file:
        for line in file:
            if line.strip() == password:
                print("Password is exposed!")
                break


# Method used to find the range.
def categorize_characters(password):
    result = {
        "lowercase": [],
        "uppercase": [],
        "digits": [],
        "shift_0_9_symbols": [],
        "other_symbols": []
    }
    shift_0_9_symbols = "!@#$%^&*()"

    for char in password:
        if char.islower():
            result["lowercase"].append(char)
        elif char.isupper():
            result["uppercase"].append(char)
        elif char.isdigit():
            result["digits"].append(char)
        elif char in shift_0_9_symbols:
            result["shift_0_9_symbols"].append(char)
        elif char in string.punctuation:
            result["other_symbols"].append(char)
    return result


# Method used to identify the range's total.
def cal_range(resultsArray, ):
    weights = {
        "lowercase": lc,
        "uppercase": uc,
        "digits": num,
        "shift_0_9_bols": sym,
        "other_symbols": oSym
    }
    range = sum(weights[k] for k, v in resultsArray.items() if v)
    return range


# Accepts user input and calculates entropy, and runs password_exposed_check.
while True:
    password = input("Please enter your password:")
    categorized = categorize_characters(password)
   
    # Entropy formula E = log2(R^L)
    range = cal_range(categorized)
    passwordLength = len(password)
    entropy = passwordLength * math.log2(range)
    password_exposed_check(password)

    if entropy <= 35:
        print("your password is very weak.\n")
    elif entropy <= 59:
        print("your password is weak.\n")
    elif entropy <= 119:
        print("your password is strong.\n")
    else:
        print("your password is very strong.\n")
