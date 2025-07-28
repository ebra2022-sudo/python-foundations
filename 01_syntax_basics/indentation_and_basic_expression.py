# Let's go step-by-step to clearly understand indentation and basic expressions in Python —
# from beginner to foundational level:

# 1. What Is Indentation in Python?

"""
Indentation is how you define code blocks in Python.
Unlike languages like C, Java, or JavaScript which use { } to mark blocks,
Python uses indentation (spaces or tabs) to group statements.
"""

# Example:

x = 2
if x > 0:
    print("Positive number")
    print("Still inside if")
print("Outside if")

"""
⚠️ Indentation Rules:
    Use 4 spaces per indentation level (standard in PEP 8) but we can use any space number as long as we keep consistency.

    Never mix tabs and spaces(i.e. indentation consistency is mandatory).

    Incorrect indentation raises IndentationError(for example if we leave indentation after we open the colon).
"""

# 2. Basic Expressions in Python

# An expression is anything that can be evaluated to a value.

"""
Common type expression:
| Expression Type | Example          | Result          |
| --------------- | ---------------- | --------------- |
| Arithmetic      | `3 + 4`          | `7`             |
| Comparison      | `5 > 2`          | `True`          |
| Assignment      | `x = 10`         | assigns 10 to x |
| Logical         | `True and False` | `False`         |
| String          | `"Hi" + "!"`     | `"Hi!"`         |
| List            | `[1, 2] + [3]`   | `[1, 2, 3]`     |


Special Types of Expressions:
 
Boolean Expressions: Result is True or False
a == b, x in list, not flag

Membership: 'a' in 'cat' → True

Identity: x is y → checks object identity
"""

# 3. Expression vs Statement

# Expression: evaluates to a value → 2 + 2
# Statement: performs an action → x = 4 (assignment)

# do all statements have side effect?
# No, not all statements have side effects.
