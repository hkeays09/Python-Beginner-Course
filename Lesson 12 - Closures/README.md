### 🔧 What I did
- Learned what a **closure** is: a function that remembers variables from its parent scope even after the parent has finished running
- Created a closure (`parent_function`) to track and update a coin count without using global variables
- Used `nonlocal` inside closures to update variables from the enclosing scope
- Updated the Rock, Paper, Scissors game to:
  - Use closures to track game stats (`game_count`, `player_wins`, `python_wins`)
  - Keep state between multiple plays without relying on global variables
  - Encapsulate logic and variables inside the main `rps()` function

### ⚠️ What went wrong
- Initially had to adjust where `nonlocal` was used to make sure stats updated correctly
- Learned that forgetting `nonlocal` inside nested functions causes new variables to be created instead of updating the existing ones

### 🧠 What I learned
- **Closures** allow functions to “remember” and update data from their parent function’s scope
- **`nonlocal`** lets you modify variables in the nearest enclosing scope (not global scope)
- Closures are a cleaner alternative to global variables for storing state
- Nested functions can be used to organize logic while keeping related data private
- This pattern is useful for games, counters, and any feature that needs persistent data without external storage

### 💭 Reflection
A lesson which builds upon scopes. Once again clearing up the global variables, and making code clean and concise.