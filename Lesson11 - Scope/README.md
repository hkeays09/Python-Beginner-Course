## 📘 Lesson 11 – Scope, Global, and Nonlocal Variables

### 🔧 What I did
- Learned about **variable scope** in Python (local, nonlocal, global)
- Used `global` to modify variables defined outside a function
- Used `nonlocal` to modify variables from an enclosing function
- Nested functions to see how variables behave in different scopes
- Updated the Rock, Paper, Scissors game to:
  - Track number of games played using a global variable
  - Structure winner logic in a nested `decide_winner()` function
  - Keep replay functionality inside the main game loop

### ⚠️ What went wrong
- Realsised that version 3 was not calling the function again when y was pressed (just returning it). Added some brackets after return play_again to make it work. I.e. "return play_again()"

### 🧠 What I learned
- **Local scope:** Variables declared inside a function are only accessible there
- **Global scope:** Variables declared outside functions can be accessed anywhere — but to modify them inside a function, you must declare `global varname`
- **Nonlocal scope:** Used inside nested functions to modify variables in the nearest enclosing scope
- Global variables should be used sparingly — better to pass values between functions when possible
- Nested functions can make code more organized, but require careful handling of variable scope

### 💭 Reflection
Another edit which was found quickly with AI. I have worked with MATLAB before AI, and small errors like this would take hours to find.

It may have been due to it being my first programming languague. Typically I would end up scanning my entire code (if my deduction for an error seemed wrong). Sometimes I would even retype the entire thing.

I would always get it to work, but it took way longer. This is a fantastic tool, facilitating my learning and course progression.