# 1. Data types in python

"""
Python is a dynamically typed language, which means variables don’t require an explicit declaration
to reserve memory space — the interpreter allocates memory dynamically when the value is assigned.

A: Basic Built-in Data Types
| Type       | Description                                | Example            |
| ---------- | ------------------------------------------ | ------------------ |
| `int`      | Integer numbers (whole numbers)            | `x = 5`            |
| `float`    | Floating-point numbers (decimals)          | `y = 3.14`         |
| `bool`     | Boolean values (`True` or `False`)         | `flag = True`      |
| `str`      | String of characters                       | `name = "Ebrahim"` |
| `NoneType` | Special type representing absence of value | `a = None`         |


B: Collection Data Types
| Type    | Description                                    | Example                  |
| ------- | ---------------------------------------------- | ------------------------ |
| `list`  | Ordered, mutable, allows duplicate elements    | `nums = [1, 2, 3]`       |
| `tuple` | Ordered, immutable                             | `point = (3, 4)`         |
| `set`   | Unordered, mutable, no duplicates              | `items = {1, 2, 3}`      |
| `dict`  | Key-value pairs, unordered (as of Python 3.6+) | `user = {"name": "Ali"}` |

C: Advanced or Custom Types
| Type                      | Description                              | Example                        |
| ------------------------- | ---------------------------------------- | ------------------------------ |
| `complex`                 | Complex numbers (`a + bj`)               | `z = 2 + 3j`                   |
| `bytes`, `bytearray`      | Binary sequences (immutable/mutable)     | `b = b"abc"`                   |
| `memoryview`              | Memory-efficient view of binary data     | `mv = memoryview(b"hello")`    |
| `range`                   | Immutable sequence of numbers            | `r = range(5)`                 |
| `enumerate`, `zip`, etc.  | Iterators returned by built-in functions | `for i, v in enumerate(items)` |
| `user-defined classes`    | Custom object types                      | `class Car: ...`               |
| `NamedTuple`, `dataclass` | Struct-like types (Python 3.6+, 3.7+)    | `@dataclass class User: ...`   |


"""

# 2. Type Casting in Python (Type Conversion)

"""
Casting means converting the value from one type to another. Python supports both implicit and explicit casting.

"""

# Implicit Type Conversion
# Python automatically converts types when no data is lost
# Example
a = 10      # int
b = 5.5     # float
c = a + b   # float (automatically converted - the type for variable "a" cast to a float type)
print(c)    # 15.5

# Explicit Type Conversion (Type Casting)
# Use built-in functions to force a type change.

# Convert float to int
x = int(5.9)        # 5

# Convert string to int
y = int("100")      # 100

# Convert int to float
z = float(3)        # 3.0

# Convert list to set
s = set([1, 2, 3, 3])  # {1, 2, 3}

# Convert string to list
lst = list("abc")     # ['a', 'b', 'c']

# ⚠️ Casting between incompatible types raises ValueError:
# int("abc")  # ValueError

# 3. Naming Conventions in Python

"""
Variable Naming Rules
Must start with a letter (a-z, A-Z) or underscore (_)

Can include digits (0–9)

Case-sensitive (name ≠ Name)

Can't use reserved keywords (if, else, class, etc.)

Naming Styles

| Style              | Example                  | Usage                                 |
| ------------------ | ------------------------ | ------------------------------------- |
| `snake_case`       | `user_name`, `max_value` | Variables, functions                  |
| `UPPER_CASE`       | `PI`, `MAX_LENGTH`       | Constants                             |
| `camelCase`        | `userName`               | Rare in Python (common in JS/Java)    |
| `PascalCase`       | `UserProfile`, `MyClass` | Class names                           |
| `_single_leading`  | `_temp`                  | "Private" variables (convention only) |
| `__double_leading` | `__init__`               | Name mangling in classes              |
| `__double__both__` | `__str__`, `__len__`     | Magic/dunder methods                  |



"""

# Valid names
age = 25
user_name = "Ali"
_score = 80

# Invalid names
# 2user = "Error" due to strat with number digit
# user-name = "Error" due to invalid character "-"

