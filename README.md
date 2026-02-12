*This project has been created as part of the 42 curriculum by khhammou*

# Pre-requisites to understand:


How to run a pythin file?

First when python runs a file, it sets a special variable:

__name__

If the file is executed directly(python3 file.py)

then __name__ == "__main__"

If file is imported:

import file

then __name__ == "file"

so when we do

if __name__ == "__main__":

it means only run this block if the file is executed directly

if we import and remove the if check

then the code runs immediatly during import

just importing the file executes its code and you lose control

This is bad because you dont want test code running automatically

so the if check stops it from running automatically when imported basically

Shebang line:

#!/usr/bin/env python3

It tells the OS use python 3 to execute this file

with shabang instead of doing python3 script.py

you can do ./script.py

/env searches for python3 in your system PATH

Rename remotes and current branch:

git remote rename origin github

git branch -m master

Reminder about some python syntax:

range(i, b)

for i in range(0, 5)

means i starts at 0 and while i < 5 we iterate and it increments


Class vs Object:

Class is the blueprint

example:

class ClassName():

    attr: attr type
    
    age: int


object is a real instance created from the blueprint

Each object has its own values

__init__ is the constructor

It runs automatically when you create a new object like

rose = className(attr1, attr2, attr3)

It sets up self.attr1 and same for the other 2 attrs

defined like:

def __init__(self, attr1, attr2, attr3):

    self.attr1 = attr1

    etc..

What does self mean?


self means this specific object

if u create like

rose = className("rose", 2, 30)

then inside the class

self.name refers to rose.name



you need self to modify the instance

classes are not defined with parameters in paranthesis, thats only for inheritance

self means specific for this object


so we can do rose.name and sunflower.name and each obj stores its own attributes

class Plant():
        name: str


        height: int
        age: int


writing it like this just creates class 


annotations not instance variables


Each object won't get those attributes




class annotations are like metadata and type 



hints and are not instances variables and methods 


that can be used


when you call a method on an object, python sends 



the object itself as self, as a parameter so if 


your method is defined like def get_help(self, name)

when used in code u create a object car for 


example


and you can do car.get_help("Camaro")

and car the object would be passed as a hidden 

parameter implicitly you could say

zip is one of python's most useful tools for working with multiple sequences at the same time:

zip()
It takes 2 or more lists(or any iterable) and coombines them element by element into tuples

example:
names = ["rose", "cactus", "oak"]
heights = [25, 500, 5]

for n, h in zip(names, heights):
    print(n, h)
first element of names pairs with first element of heights
it is like
Plant(names[x], heights[x], ages[x]) done n times
instead you can do
Plant(n, h, a) for n, h, a in zip(names, heights, ages)
Notes:
if your lists are diff lengths, zip() stops at the shortest list

plants = [] created an empty list
plants.append() is a method that adds items to the list
plants = [Plant(n, h, a) for n, h, a in zip(names, heights, ages)]
This is a shorter cleaner version of the creation to avoid appending item by item
Encapsulation / data hiding:
done by prefixing variables with _(protected)
or __ (private) to discourage direct access
example:
self.__height = height
public can be accessed anywhere
protected can still be accessed anywhere it just shows internal hints not strict
private can be accessed only inside the class and very strict and forces you to use your setters and getters
Inheritance is doen by building SecurePlant class starting from your Plant class
inside __init__ if invalid age or height you cant return anything like return "" you can only return none
which means you could print but you cannot do return "this is invalid"
## Description

### Instructions


## Resources



## AI Usage

