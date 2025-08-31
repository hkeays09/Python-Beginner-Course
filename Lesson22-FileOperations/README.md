## 📘 Lesson 22 – File Handling in Python  

### 🔧 What I did  
- Practiced **file operations** with Python’s built-in `open()` function:  
  - **Read (`r`)** – opened and read file contents (with `.read()`, `.readline()`, and iteration).  
  - **Append (`a`)** – added new content (`"Neil"`) without overwriting existing data.  
  - **Write (`w`)** – overwrote files or created new ones.  
  - **Create (`x`)** – created a file but raised an error if it already existed.  
- Used `os.path.exists()` to safely check if a file exists before creating or deleting.  
- Learned to **delete files** with `os.remove()` while avoiding errors if the file didn’t exist.  
- Practiced the `with open(...) as f:` context manager to automatically handle file closing.  
- Copied contents from one file (`more_names.txt`) into another (`names.txt`).  

### ⚠️ What went wrong  
N/A  

### 🧠 What I learned  
- Modes:  
  - `r` → read (error if file doesn’t exist)  
  - `a` → append (creates if missing)  
  - `w` → write/overwrite (creates if missing)  
  - `x` → exclusive create (error if exists)  
- Always close files after use (or rely on `with open()` for automatic cleanup).  
- Use `os.path.exists()` for safe file handling before creating/deleting.  
- File handling is essential for persisting data beyond a single script run.
- Risk of forgetting to `close()` files after opening them — fixed by using the **`with` context manager**.  
- Not checking for file existence before creating/deleting could lead to errors

### 💭 Reflection  
This lesson gave me hands-on experience with how Python interacts with the filesystem. I now understand the differences between reading, writing, appending, and creating files, and how to safely manage them. Using `with open()` feels much cleaner and prevents mistakes. This is a crucial step toward building real applications that read/write data.  
