# Scalable Sequence Generator

A professional Python tool for generating and managing numerical sequences (like Fibonacci) with high memory efficiency and data persistence. This project demonstrates how to handle large datasets using modern Pythonic patterns.

## Key Features

* **Memory Efficient:** Uses **Python Generators** (`yield`) to handle extremely large sequences without overloading RAM.
* **Context Management:** Implements custom **Context Managers** (`__enter__`, `__exit__`) for safe, automated file I/O operations and resource handling.
* **Object-Oriented Design:** Built with clean, modular classes following the **DRY** (Don't Repeat Yourself) principle.
* **Robust Validation:** Includes strict error handling to ensure data integrity during initialization and sequence calculation.
* **Professional Testing:** Comprehensive test suite built with **pytest**, utilizing advanced features like fixtures and parameterization.

## Tech Stack

* **Language:** Python 3.9+
* **Testing:** Pytest
* **Storage:** Flat-file (TXT) with planned SQL Integration

## Project Structure

```text
├── main.py              # Core logic & SequenceGenerator class
├── tests/
│   └── tests.py         # Professional test suite (Logic & I/O)
├── requirements.txt     # Project dependencies
└── .flake8              # Linter configuration
```

## Testing

The project uses `pytest` to ensure code reliability and data integrity. The test suite covers generator logic, edge cases, and file I/O operations.
  
### 1. Install Testing Dependencies
Ensure you have `pytest` installed in your environment:
```bash
pip install pytest
```
### 2. Use command
```console
pytest tests/tests.py
```
