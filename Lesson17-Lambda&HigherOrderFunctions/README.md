## 📘 Lesson 17 – Lambdas, Map, Filter & Reduce  

### 🔧 What I did  
- Practiced **lambda functions** (short, anonymous functions)  
- Rewrote normal functions (`squared`, `addTwo`, `sum_total`) as lambdas  
- Created functions that return lambdas (closures) with `funcBuilder`  
- Used:  
  - **`map()`** → apply a lambda to each item in a list (`squared_nums`)  
  - **`filter()`** → keep only odd numbers from a list (`odd_nums`)  
  - **`reduce()`** → combine a list into a single value (sum, char count, etc.)  

### ⚠️ What went wrong  
- Nothing major — just had to remember that `map`, `filter`, and `reduce` return iterators, so you often need to wrap them in `list()` to see results.  

### 🧠 What I learned  
- **Lambdas** are useful for quick, one-off functions you don’t want to define separately  
- **Higher-order functions** (`map`, `filter`, `reduce`) make code shorter and more expressive than loops  
- `reduce()` can be replaced by built-in functions like `sum()`, but is powerful for more complex operations  

### 💭 Reflection  
- This style of functional programming is clean and efficient. But the concepts are beginning to layer over eachother so I need to be careful with my understanding. For example, with closures where we were using nested functions (aka higher order functions). So overall made sense.
