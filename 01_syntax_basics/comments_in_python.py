# 1. Basic Single-Line Comments

# use hashtag(#) for single line comment
# Best for Brief explanation of a line or block,
# This is a single-line comment
x = 5  # You can also write after code



# 2. Multi-line Comments (unofficial)

# Python doesn’t have true multiline comments, but you can simulate them by repeating #.
# This is a comment
# that spans multiple lines
# and explains something in detail.



# 3. Docstrings (Documentation Strings)

# These are special strings used to describe modules, classes, functions, or methods.
# Docstrings are surrounded by triple quotes: """ or '''.
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

class Printer:
    """ This is printer class to model the printer object."""
    def start_printer(self):
        print("The printer is on")

# They are not comments, technically — they're actual string objects attached to the function/class/module, accessible via:
print(greet.__doc__) # this prints 'Return a greeting message for the given name.'
print(Printer.__doc__) # this prints 'This is printer class to model the printer object.'



# 4. Multi-line Docstrings (Advanced Format)

# Used for documenting APIs or libraries, with formatting conventions (like PEP 257 and reStructuredText).
# To see the documentation for this function, hover over the function name using your mouse if you use code editor
# or log using print(<Function/Class Name>.__doc__)
def add(x, y):
    """
    Add two numbers.

    Parameters:
    x (int): The first number.
    y (int): The second number.

    Returns:
    int: The sum of x and y.
    """
    return x + y



# 5. Module-Level Docstring

# Put this at the top of .py files to describe the purpose of the file
"""
math_utils.py

Provides utility functions for mathematical operations.
"""



# 6. Commenting Out Code

# Temporarily disable certain code of line
# To comment out like this line print("This line is commented out")
# ctrl + / fo comment out a current cursor line or currently selected lines



# 7. Special Comments

# TODO: – Marks unfinished work.

# FIXME: – Marks broken or buggy code.

# NOTE: – Highlights important info.

# HACK: – Indicates workaround.

# WARNING: – Cautions about risky code.



"""
Best Practices for Professional Comments:

Tip	                                   Why

Be concise	                        Comments should clarify, not clutter.
Explain why, not just what      	Code shows what; comments explain reasoning.
Use docstrings for public APIs	    Makes it easy to generate documentation.
Keep them up to date	            Outdated comments are misleading.
Avoid obvious comments	            Don't write # increment x for x += 1.

"""