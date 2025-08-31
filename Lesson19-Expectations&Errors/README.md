## 📘 Lesson 19 – Exceptions & Error Handling  

### 🔧 What I did  
- Created a **custom exception** class `JustNotCoolError` that inherits from `Exception`.  
- Used `try/except` blocks to handle different types of errors:  
  - `NameError` → when a variable is undefined  
  - `ZeroDivisionError` → when dividing by zero  
  - General `Exception` → catches any other errors, including custom ones  
- Practiced raising exceptions with `raise` (e.g., forcing errors for testing).  
- Added `else` (runs only if no errors occur) and `finally` (always runs, error or not).  

### ⚠️ What went wrong  
- Needed to be careful with indentation and making sure the right exception type is caught.  
- Custom exceptions must inherit from `Exception`.  

### 🧠 What I learned  
- `try/except` lets you handle specific errors gracefully without crashing the program.  
- `else` runs only when no exception is raised.  
- `finally` is guaranteed to run no matter what (useful for cleanup like closing files).  
- You can raise your own **custom exceptions** to signal special conditions in your code.  

### 💭 Reflection  
- Exception handling makes programs more robust and user-friendly.  
- Custom exceptions are a powerful way to create more descriptive error handling in bigger projects.  
