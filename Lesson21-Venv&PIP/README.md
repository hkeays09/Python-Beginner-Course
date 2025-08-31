## 📘 Lesson 21 – Virtual Environments, PIP & Weather API Project

### 🔧 What I did
- Learned how to use **PIP** to install, uninstall, and manage Python packages (`requests`, `python-dotenv`).
- Created a **virtual environment (venv)** with `py -m venv .venv` and practiced activating/deactivating it.
- Generated a `requirements.txt` file with `py -m pip freeze > requirements.txt` to track dependencies.
- Built a **Weather App** that:
  - Reads a city name from user input
  - Loads a hidden API key from a `.env` file with `dotenv`
  - Calls the OpenWeather API with `requests`
  - Parses and displays JSON response data (temperature, feels-like, description)

### ⚠️ What went wrong
- At first, `os.getenv("API_KEY")` returned `None` because `.env` wasn’t being picked up.
- Solved by ensuring `python-dotenv` was installed in the correct venv and refreshing the environment.
- PowerShell blocked `.venv\Scripts\Activate.ps1` due to execution policy — worked around it with direct `python.exe` calls or temporary bypass.

### 🧠 What I learned
- **PIP** is the package manager for Python; it installs packages locally inside a project’s venv.
- **Virtual environments** isolate project dependencies so packages don’t clash across projects.
- `.env` files store **secrets** (like API keys) safely outside code and must be excluded from GitHub.
- `requests.get(...).json()` makes it easy to fetch and parse API data.
- Pretty-printing with `pprint` or formatted f-strings improves readability.
- Good practice: confirm `.env` loads before building request URLs.

### 💭 Reflection
This was a loaded but rewarding lesson - I set up my first real API - driven script, while also learning how to manage Python environments and dependencies properly. Now I understand why venvs, pip, and secrets management are essential in real-world projects.
