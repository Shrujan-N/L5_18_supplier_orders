# Issues Documented - Lab 5 Static Code Analysis

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Command Injection (B605/B607)** | Security (Bandit) | 20 | Executing `os.system()` with string concatenation allows shell injection vulnerabilities. | Replaced `os.system` with native `print()` statement to eliminate external process calls. |
| **SQL Injection (B608)** | Security (Bandit) | 12 | Using string formatting (`%s`) in SQL queries allows SQL injection attacks. | Converted query to use parameterized placeholders (`?`) with tuple binding. |
| **Global State Mutation (W0603)** | Quality (Pylint) | 10 | Use of `global order_total` creates tight coupling and side effects across calls. | Passed `current_total` as an explicit argument and returned the updated value. |
| **Broad Exception Catching (W0703)** | Bug/Quality (Pylint) | 24-25 | `except Exception: pass` silently suppresses all errors including syntax bugs. | Replaced with specific `sqlite3.Error` handling and printed informative error log. |
| **Naming Conventions & Formatting (C0103/PEP8)** | Style (Pylint/Flake8) | Multiple | Functions used `camelCase` (`placeOrder`) and lacked docstrings/2-line spacing. | Renamed functions to `snake_case`, added module/function docstrings, and fixed PEP 8 blank line spacing. |
| **Unused Parameter (W0612)** | Code Quality (Pylint) | 15 | Parameter `remarks` was declared in `markReceived` but never utilized. | Retained optional parameter signature with explicit usage assignment `_ = remarks`. |
