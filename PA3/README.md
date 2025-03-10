# Numerical Methods Implementation - Assignment 3

This project implements numerical methods for solving differential equations, specifically:
1. Euler Method
2. Runge-Kutta Method (4th order)

## Requirements

The project requires NumPy library. You can install it using:

```bash
pip install -r requirements.txt
```

## Running the Program

To run the main program from the command line, navigate to the project root directory and execute:

```bash
python src/main/assignment_3.py
```

## Running Tests

To run the tests, execute:

```bash
python -m unittest src/test/test_assignment_3.py
```

## Project Structure

```
.
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │   └── assignment_3.py
│   └── test/
│       ├── __init__.py
│       └── test_assignment_3.py
├── requirements.txt
└── README.md
``` 