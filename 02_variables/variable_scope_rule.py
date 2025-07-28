"""
variable_scope_rule.py
variable scoping rules in python from basic to advanced
"""
# Scope defines where in your code a variable is visible or accessible
# Python’s 4 Levels of Scope – The LEGB Rule

"""
| Level | Meaning       | Where it Applies                                      |
| ----- | ------------- | ----------------------------------------------------- |
| **L** | **Local**     | Inside a function or lambda                           |
| **E** | **Enclosing** | Inside nested functions (outer function of a closure) |
| **G** | **Global**    | At the top-level of the script or module              |
| **B** | **Built-in**  | Python’s built-in names (like `len`, `print`)         |


+---------------------+
| Built-in Scope      | ← Python built-ins like len(), print(), range() that python interpreter can import automatically with out the need of explicit import
+---------------------+
         ↑
+---------------------+
| Global Scope        | ← Module-level variables
+---------------------+
         ↑
+---------------------+
| Enclosing Scope     | ← Variables from outer functions
+---------------------+
         ↑
+---------------------+
| Local Scope         | ← Variables in current function
+---------------------+

NOTE: python searches from bottom to top (L → E → G → B) or innermost to outermost. If the name isn't found, it raises NameError


"""

# Example:

x = "global"  # Global


def outer() :
    x = "enclosing"  # Enclosing
    def inner() :
        x = "local"  # Local
        print(x)

    inner()


outer()  # Output: "local"

x = 5

def func():
    # global x use this declaration or remove the second x = 10 as it makes the interpreter to expect local x before print
    # print(x)
    x = 10 # Shadows name 'x' from outer scope

func()

def greet():
    name = "Ebrahim"
    print(name)

greet()
# print(name)  # ❌ Error: name is not defined outside


# Advanced Scope Topics

# 1. Closures

# Inner functions remember enclosing variables even after the outer function finishes.

# In essence, the outer function is higher order function thet return an inner function with type () -> None
def outer() :
    msg = "Hello"

    def inner() :
        print(msg)

    return inner


f = outer()
f()  # prints "Hello"

# 2. Global Scope Across Modules

# In module_a.py
# x = 10
#
# # In module_b.py
# import module_a
# print(module_a.x)  # Access module_a's global

# 3. Comprehensions Have Local Scope

x = 10
print([x for x in range(5)])  # `x` here doesn't affect the global x
print(x)  # still 10
# summary table


"""
| Scope Type | Keyword    | Can be modified? | Applies to               |
| ---------- | ---------- | ---------------- | ------------------------ |
| Local      | —          | Yes              | Inside function          |
| Enclosing  | `nonlocal` | Yes              | Nested functions         |
| Global     | `global`   | Yes              | Entire module            |
| Built-in   | —          | No               | `len()`, `print()`, etc. |

"""

x = "global"


def outer() :
    x = "enclosing"

    def inner() :
        x = "local"
        print("Inner:", x)

    inner()
    print("Outer:", x)


outer()
print("Global:", x)

# Best Practices for Managing Scope in Real Projects

"""
| Rule                                                                              |
| --------------------------------------------------------------------------------- | 
| Use `global` when **modifying global variables** inside a function                |         
| Use `nonlocal` when modifying **outer function variables** inside inner functions |         
| Python resolves variables using **LEGB rule**                                     |         
| Avoid overwriting **built-ins** (like `list`, `str`, `input`)                     |         
| Closures capture enclosing scope variables automatically                          |         
| Keep variable lifetimes as **short and clear** as possible                        |         

"""