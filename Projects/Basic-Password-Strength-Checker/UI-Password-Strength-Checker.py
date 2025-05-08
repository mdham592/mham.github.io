# Mason Ham
# Basic Password Strength Checker With UI
# SDK Python 3.8


import math
import string
import tkinter as tk
from tkinter import DISABLED

# If you use Lowercase Letters, Uppercase Letters, Numbers, Shift + [0-9] Symbols, and Other Symbols. If all character types are uses the range can reach 95.
lc = 26
uc = 26
num = 10
Sym = 10
oSym = 23

# Method to check password against know exposed password lists
def password_exposed_check(password):
    with open(r'D:\projects\10k-common-passwords.txt', 'r') as file:
        for line in file:
            if line.strip() == password:
                return True
    return False

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

# Method used to identify the ranges total.
def cal_range(resultsArray):
    weights = {
        "lowercase": lc,
        "uppercase": uc,
        "digits": num,
        "shift_0_9_symbols": Sym,
        "other_symbols": oSym
    }
    return sum(weights[k] for k, v in resultsArray.items() if v)



# GUI Logic
def save_input():
    password = text_area.get("1.0", tk.END).strip()
    text_area.delete("1.0", tk.END)
    categorized = categorize_characters(password)
    range = cal_range(categorized)
    length = len(password)

    if range == 0 or length == 0:
        result_label.config(text="Invalid password input.")
        return

    # Entropy formula E = log2(R^L)
    entropy = length * math.log2(range)
    exposed = password_exposed_check(password)

    result = f"Entropy: {entropy:.2f}\n"

    if exposed:
        result += "⚠️Password is exposed!\n"

    if entropy <= 35:
        result += "Your password is VERY WEAK."
    elif entropy <= 59:
        result += "Your password is WEAK."
    elif entropy <= 119:
        result += "Your password is STRONG."
    else:
        result += "Your password is VERY STRONG."

    result_label.config(text=result)

# Setup UI
root = tk.Tk()
root.title("Basic Password Strength Checker")
root.geometry("600x500")

text_widget = tk.Text(root, height=2)
text_widget.insert("1.0", "Hello, please enter your password!\n")
text_widget.tag_configure("center", justify="center")
text_widget.tag_add("center", "1.0", "end")
text_widget.config(state=DISABLED)
text_widget.pack()

text_area = tk.Text(root, height=3, width=40)
text_area.pack()

save_button = tk.Button(root, text="Check Password", command=save_input)
save_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=500, justify="center", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()