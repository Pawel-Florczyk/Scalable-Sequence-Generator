# Scalable Sequence Generator

A professional Python tool for generating, managing, and streaming high-volume numerical sequences (like Fibonacci). Engineered for ultimate memory efficiency and seamless data persistence, this project demonstrates modern Pythonic patterns for large-scale data processing. It serves as a robust foundation for Big Data pipelines and analytics.

---

## Key Features

* **Memory Efficient:** Uses Python Generators (`yield`) to handle extremely large sequences without overloading RAM.
* **Context Management:** Implements custom Context Managers (`__enter__`, `__exit__`) for safe, automated file I/O operations and resource handling.
* **Object-Oriented Design:** Built with clean, modular classes following the DRY (Don't Repeat Yourself) principle.
* **Robust Validation:** Includes strict error handling to ensure data integrity during initialization and sequence calculation.
* **Professional Testing:** Comprehensive test suite built with `pytest`, utilizing advanced features like fixtures and parameterization.

---

## Tech Stack

* **Language:** Python 3.12
* **Containerization:** Docker & Docker Compose
* **Testing:** Pytest
* **Storage:** Flat-file (TXT) with planned SQL Integration

---

## Project Structure

```text
├── main.py              # Core logic & SequenceGenerator class
├── tests/
│   └── tests.py         # Professional test suite (Logic & I/O)
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Multi-container/service orchestration
├── requirements.txt     # Project dependencies
└── .flake8              # Linter configuration
```

## Running Tests via Docker Compose
```bash
docker compose up test-runner
```

## Running Tests via Docker:

1. Building an image
```bash
docker build -t scalable-sequence-generator .
```

2. Running container with tests
```bash
docker run -v .:/app scalable-sequence-generator pytest tests/tests.py
```
## Local testing (without docker):

1. Install Testing Dependencies
Ensure you have pytest installed in your environment:
```bash
pip install pytest
```

2. Use command
```bash
pytest tests/tests.py
```
