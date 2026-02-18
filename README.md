# 🌱 Python OOP Project – 42 Curriculum

*Created as part of the 42 curriculum by khhammou*

---

# 📌 Pre-requisites

## ▶️ How to Run a Python File

When Python runs a file, it sets a special variable:

```python
__name__
```

* If executed directly:

```bash
python3 file.py
```

Then `__name__ == "__main__"`

* If imported:

```python
import file
```

Then `__name__ == "file"`

### Why use:

```python
if __name__ == "__main__":
```

Only runs the code when the file is executed directly, not on import.

---

## 🐍 Shebang Line

```bash
#!/usr/bin/env python3
```

Allows execution via `./script.py` instead of `python3 script.py`.

---

## 🔁 Git Quick Tips

```bash
git remote rename origin github
git branch -m master
git pull --rebase
git push --force
git reset --hard origin/master
```

---

# 🧠 Python Concepts Review

## 🔄 range()

```python
for i in range(0, 5):
```

* Starts at 0, stops before 5

---

## 🏗 Class vs Object

### Class

Blueprint definition:

```python
class Plant:
    name: str
    height: int
```

(Type annotations, not instance variables)

### Object

Instance of a class:

```python
rose = Plant("Rose", 20)
```

---

## 🛠 **init** Constructor

```python
def __init__(self, name, height):
    self.name = name
    self.height = height
```

`self` refers to the current object.

---

## 🔑 What is `self`?

Python automatically passes the object to methods:

```python
rose.grow() # internally Plant.grow(rose)
```

---

# 🔒 Encapsulation

* Public → normal variable
* Protected → `_variable`
* Private → `__variable`

Example:

```python
self.__height = height
```

---

# 🧬 Inheritance

```python
class Child(Parent):
```

Child can override parent methods (polymorphism).
Use `super()` to call parent logic.

---

# 🏷 Getting Class Name

```python
self.__class__.__name__
```

---

# 🖨 print() vs return

### print()

* Displays immediately
* Returns None
* Cannot be reused

### return

* Sends data back to caller
* Does NOT print automatically
* Can be stored, modified, reused

Best practice: methods return data; main decides what to print.

---

# 🔗 zip()

Combines iterables element by element:

```python
for n, h in zip(names, heights):
    print(n, h)
```

Stops at the shortest list.

List comprehension:

```python
plants = [Plant(n, h) for n, h in zip(names, heights)]
```

---

# 🧱 Class Variables

Shared across all instances:

```python
class Garden:
    total_gardens = 0
```

---

# 🏛 Class Methods

```python
@classmethod
def method(cls):
    cls.class_var = 0
```

* Access class itself
* Modify class variables

---

To increment or decrement a variable you must first initialize it to a value
else it would throw a UnboundLocalError

# 🧰 Static Methods

```python
@staticmethod
def add(x, y):
    return x + y
```

* Belongs to class
* No access to `self` or `cls`

---

# 📏 Code Style (flake8)

* Max line length: 79 chars
* 1 blank line between methods
* 2 blank lines before `if __name__ == "__main__":`

---

# 📖 Project Description

Covers:

* Object-Oriented Programming
* Inheritance chains
* Encapsulation
* Class & static methods
* Clean Python practices

---

# 📚 Resources

* Python Official Documentation
* 42 Intranet Subject
* flake8 Style Guide

---

# 🤖 AI Usage

AI was used as:

* Concept clarifier
* Design reviewer
* Debugging assistant

All code logic and understanding manually validated.
