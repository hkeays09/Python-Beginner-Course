## 📘 Lesson 20 – OOP Banking Project (Classes, Inheritance & Exceptions)

### 🔧 What I did
- Built a **BankAccount** class with core methods: `getBalance`, `deposit`, `withdraw`, `transfer`.
- Added a `viableTrasaction` check that raises a **custom exception** `BalanceException` on insufficient funds.
- Created subclasses:
  - **InterestRewardsAcc** – **overrides** `deposit` to add a 5% bonus.
  - **SavingsAcc** – uses `super().__init__`, adds a `fee`, and **overrides** `withdraw` to include the fee.
- Implemented **try/except** around `withdraw` and `transfer` to handle `BalanceException` gracefully.
- Drove the classes from a runner script: created accounts, made deposits/withdrawals, and tested transfers.

### ⚠️ What went wrong
N/A

### 🧠 What I learned
- **Inheritance & overriding**: subclasses can customize behavior (e.g., bonus deposits, fee-based withdrawals).
- **`super()`** lets subclasses reuse parent initialization/logic cleanly.
- **Custom exceptions** make domain errors (like insufficient funds) explicit and easier to handle.
- Wrapping operations with **`try/except`** prevents crashes and provides user-friendly messages.
- Encapsulating account logic into methods keeps code **modular and testable**.

### 💭 Reflection
A good project going over everything we have learnt thus far relating to object oriented programming.