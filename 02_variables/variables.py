# Brainstorming questions:

"""
When I write x = 2 in a Python script:

Where is the variable name (x) stored?

What happens at editing time (before running)?

What happens at runtime (when executing)?

How are name conflicts handled in both cases?
"""

# 1. Editing Time (Before Running the Code)

# When you write:

x = 2

"""
What happens at this stage:
This line is just plain text in a .py file.

It is not yet evaluated or stored in memory.

The variable x is not stored anywhere yet — only characters x, =, and 2 exist as part of the file's contents.

No memory is allocated.

No conflict resolution happens.

Only syntax checkers (like in VS Code or PyCharm) might flag unused or conflicting names — this is not Python itself, but the IDE or linter helping you.


Editing Time  →  No actual Python variable exists.
              →  Only text written in file.
              →  No memory usage for `x` or `2` yet.

"""


#  2. Compilation Time (When the Script is First Run)

# Python is interpreted, but under the hood, CPython compiles your script into bytecode (.pyc) before execution.

"""
During compilation:
Python parses x = 2 into bytecode instructions.

It doesn’t assign value to x yet — it just builds a plan (instructions).

It checks for syntax errors and prepares variable names for the global or local namespace.
"""

# 3. Runtime (When the Script Is Running)

# When Python executes x = 2:
#
# What happens under the hood?

"""
a) Object creation:
Python checks if 2 (an int object) already exists (in the int cache: integers from -5 to 256).
(python has caching mechanism for optimization)
If it does, it reuses it; otherwise, it creates a new int object.

b) Variable assignment:
Python adds an entry to the current namespace (usually globals() if outside a function):
"""


def my_function():
    y = 20  # Local namespace
    print("Local namespace:", locals())
    print("Global namespace:", globals())

my_function()

print(globals()['x']) # prints 2
# print(locals()['y']) # this will pop KeyError: 'y' as the scope of variable y is local to my_function

"""
In Memory:

Namespace (globals()):
{
    "x": <int object at 0x0000012345> //
}

"""
# to access the virtual memory address assigned by the os at runtime we use the function called id(variable_name)
print(id(x)) # it gives the id corresponding to the virtual memory address of in the python virtual machine
print(hex(id(x))) # the hex() function is the builtin function to return the hexadecimal notation of the given integer so too for id of the variable

# 4. Name Conflict Resolution: Editing vs Runtime

"""
At Editing Time:
Python doesn’t handle conflicts — you can write:

For example when we write:
x = 5
x = "hello"

No error until runtime.

But linters (like flake8, Pyright, or MyPy) may warn you:

Variable redefined

Type confusion

Shadowing built-ins

These are IDE/editor tools, not Python itself.


At Runtime:
Python resolves variable names using the LEGB rule (as discussed before):

Local (inside the function)

Enclosing (outer function)

Global (top of the file)

Built-in (print, len, etc.)

"""

# 5, Shadowing a Built-in

list = [1, 2, 3]
print(list)  # OK

# print = 5
# print("Hello")  # ❌ TypeError: 'int' object is not callable

"""
Why?
Because you overwrote the built-in print function in your global
namespace with an int. Python resolves names at runtime using 
the LEGB rule, so now print points to 5.
"""

# 6, Where is everything stored?

"""

| What                 | Stored Where                                         | When            |
| -------------------- | ---------------------------------------------------- | --------------- |
| Variable name (`x`)  | As key in namespace dict (`globals()` or `locals()`) | At runtime      |
| Value (`2`)          | As object in heap memory (with metadata)             | At runtime      |
| Assignment (`x = 2`) | As bytecode instruction                              | At compile time |
| Text (`x = 2`)       | As plain text in `.py` file                          | At editing time |

"""

# 7, how the object is created in memory from basic type like int, string,
# boolean to a complex object that are created from custom class in python

# Let’s walk through how objects are created in memory in Python — from primitive
# types like int, str, and bool, to complex/custom class objects — step by step.

"""
Core Principle in Python
Everything in Python is an object.

Whether you assign x = 2, x = "hi", or x = MyClass(), you're creating an object in memory.

All objects are instances of a class, either:

Built-in (e.g., int, str, list, bool)

Or user-defined (custom classes)
"""
# Memory Structure of a Python Object (Internals)

"""
Every object in Python has:

Type pointer → points to the class/type (int, str, your class, etc.)

Reference count → used by garbage collector

Value / attributes → actual content (e.g., 2, "hello", etc.)

This is handled under the hood by the C structures in CPython.
"""

# A.Basic Types (Immutable Built-in Types)
# Example
x = 2

"""
What happens:
Python checks if the object 2 is already cached (small integers are cached: from -5 to 256).

If not cached, it:

Allocates memory for a new int object on the heap.

Sets its type to int.

Stores value 2.

Adds a reference to it in the current namespace: x → object(2)
they cannot be changed in-place. since they are immutable objects
"""

# B.Mutable Types (like list, dict, set)
# Example
y = [1, 2, 3] # python list definition

"""
Python:

Creates a list object in heap memory.

Sets type pointer to list.

Stores a reference to each element (1, 2, 3).

x points to that list in the namespace.

Lists and dictionaries allow in-place modification because they are mutable.
"""

# C.Custom Class Objects

class Person:
    def __init__(self, name):
        self.name = name

# create an instance of the Person class
p = Person("Ebrahim")

"""
What happens under the hood:
Class Definition:

Creates a class object named Person.

Stored in global namespace: Person → class object

Instantiation (Person("Ebrahim"))

Calls __new__() to allocate memory for a new object.

Calls __init__() to initialize it (self.name = "Ebrahim").

The new object is stored in memory (heap).

p is added to the namespace and points to the new Person instance.


In Memory:
globals(): { "Person": class, "p": <Person object at 0xABCD> }

<Person object>:
  - type: Person
  - attributes: { name: "Ebrahim" }

"""

# summary table:

"""
| Type             | Immutable? | Stored as           | Example        | Memory Use                        |
| ---------------- | ---------- | ------------------- | -------------- | --------------------------------- |
| `int`            | ✅          | Object with value   | `x = 5`        | Cached if small (−5 to 256)       |
| `str`            | ✅          | Object with value   | `x = "hi"`     | Stored with length and hash       |
| `bool`           | ✅          | Singleton object    | `x = True`     | Only two exist: `True`, `False`   |
| `list`           | ❌          | Object with refs    | `x = [1, 2]`   | Holds references to other objects |
| `dict`           | ❌          | Object with keys    | `x = {"a": 1}` | Hash table with key-value pairs   |
| `object` (class) | Depends    | Object + attributes | `x = Person()` | Custom structure with attributes  |

"""

