## 📘 Lesson 15 – Command Line Arguments

### 🔧 What I did
- Learned how to use the **`argparse`** module to accept command line arguments in Python.
- Built a **greeting script** that:
  - Takes a `--name` argument for the user’s name.
  - Takes a `--lang` argument to select a greeting language (`English`, `Spanish`, `German`).
- Updated the **Rock, Paper, Scissors** game to:
  - Accept the player’s name as a command line argument.
  - Personalise all in-game messages using that name.

### ⚠️ What went wrong
- Realised that earlier versions were not calling the function when values outside of '123' were selected. Quickly fixed this and other small formatting parts.

### 🧠 What I learned
- **`argparse`** makes it easy to create user-friendly command line interfaces.
- Adding `choices` to `argparse` arguments restricts inputs to valid options.
- The `if __name__ == "__main__":` block ensures scripts only execute when run directly, not when imported.
- Command line arguments can make scripts more reusable and interactive.

### 💭 Reflection
Was a bit confusing of a lesson. But I think the main idea is that the argparse function allows us to input variables from the command line. You also have to now call the script from the command line rather than using run when argparse is used.