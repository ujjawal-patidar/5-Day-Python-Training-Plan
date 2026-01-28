
Day 1: Python Basics & Environment Setup

Topics Covered

**Environment Setup**
Installing Python (latest version)
Setting up virtual environments (venv)
IDE/Editor setup (VS Code, PyCharm, or Jupyter)
pip and package management
Python Syntax Fundamentals

**Indentation and code structure**
Comments (single-line, multi-line)
Python naming conventions (PEP 8)

**Variables & Data Types**
Dynamic typing
int, float, complex, str, bool
Type conversion and type checking
None type

**Basic Operators**
Arithmetic operators (+, -, *, /, //, %, **)
Comparison operators (==, !=, <, >, <=, >=)
Logical operators (and, or, not)
Assignment operators (=, +=, -=, etc.)
Identity operators (is, is not)
Membership operators (in, not in)

**String Operations**
String creation and manipulation
String methods (upper, lower, strip, split, join, replace, find)
String formatting (f-strings, .format(), %)
String slicing and indexing

**Basic Input/Output**
print() function and its parameters
input() function
Basic console I/O

**Questions**
1. Write a program to swap two variables without using a third variable.
2. Create a program that takes user input for name and age, then prints a formatted message using f-strings.
3. Write a program to check if a number is even or odd using modulo operator.
4. Convert temperature from Celsius to Fahrenheit and vice versa.
5. Check if a given string is a palindrome (case-insensitive).
6. Count the frequency of each character in a string using a dictionary.
7. Write a program to format a string using all three formatting methods (%, .format(), f-strings).
8. Write a program to check if a year is a leap year.
9. Check if two strings are anagrams of each other.
10. Create a CLI calculator that performs basic arithmetic operations based on user input with input validation.

**Assignment 1 (Optional)**
Environment Configuration Script
Build a Python script that automates the developer environment setup process. This simulates real-world scenarios where developers need to configure their local environment.

Requirements:

- Check if Python is installed and print version
- Validate Python version (must be 3.8 or higher)
- Create a project directory structure (src/, tests/, docs/, logs/)
- Generate a requirements.txt file with basic packages
- Create a .gitignore file with common Python patterns
- Print a summary report with colored output (use ANSI escape codes)
- Handle errors gracefully with try-except blocks

**Real-World Application:** DevOps teams use similar scripts to automate environment setup for new developers joining the team.