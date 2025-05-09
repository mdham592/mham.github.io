
# Basic Password Strength Checker
[Source Code without GUI](./Password-Strength-Checker.py).

[Source Code with UI](./UI-Password-Strength-Checker.py).

### Resources used:

https://docs.python.org/3/library/tk.html

https://gist.github.com/richardkundl/b68afdcf68240dcff50a

## What did I learn?
Creating a basic password strength tester reinforced many foundational programming and security concepts.

From a coding perspective, I reviewed how to manipulate strings to check things like length, the use of uppercase/lowercase letters, digits, and special characters. It also gave me hands-on practice with control flow (if/else statements).I broke the logic into functions to keep things clean and readable, and used basic data structures like arrays and sets where needed.

On the security side, I reviewed what makes a password strong, like the length, character variety, and avoiding common passwords. This also helped me realize the limitations of client-side password checkers; they can give guidance, but they don't guarantee security.

Building the password test was a solid mini-project. It touched on real-world relevance since password strength is something every app deals with. It gave me a refresher in Python and helped me learn the basics of the Tkinter package. Creating a basic password strength tester was a fun project that covered  skills across programming, security, and even user experience.


## Screenshots of the program in action
![Intraction_Screenshot.PNG](./Intraction_Screenshot.png) ![UI_Screenshot.PNG](./UI_Screenshot.PNG)


## Brief Code Walk Through

The first part of the program compares the password to the top 10,000 passwords used. A bigger password list can easily expand this.

![Exposed_password_check.PNG](./Exposed_password_check.PNG)


This part of this program identifies the types of chars used so we can calculate the range in the next step.

![identifies_chars_used.PNG](./identifies_chars_used.PNG)


Now that we know what types of chars are used, we can add up the total value of the range.

![Range_calc.PNG](./Range_calc.PNG)


This runs the program forever, accepting user input and printing out the entropy results.

![main.PNG](./main.PNG)


This is a part of the GUI program, specifically using the Tkinter package.

![UI.PNG](./UI.PNG)



## Future Improvements

If I wanted to improve this project in the future, the first thing that I would do is add regex/pattern matching when reviewing the user's password. For example, we know password123 is going to be considered weak, but if we had regex for "password," we could let the user know that their password is still super weak. We could also search for passwords that are just repetitions, such as "121212121212."








```
