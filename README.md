# naya-oops-first-practice

## Intro

This is a small beginning of writing Python code using the concepts of **classes** and **objects**.

Python is an **object-oriented programming (OOP)** language.

- A **class** is like an object constructor or a blueprint for creating objects. It is defined using the `class` keyword.
- An **object** is an instance of a class.
- Everything in Python is an object with its own properties (attributes) and methods (functions).

## Learning Base

This practice is based on the **W3Schools** tutorials. I read about:

- Python Classes and Objects
- Properties (Attributes)
- Class Attributes and Instance Attributes
- encapsulation


This repository contains my beginner practice while learning the fundamentals of Object-Oriented Programming in Python.
## updating this for library:

I extended this project by creating a **Library** class that stores and manages multiple **Book** objects.
The `Library` class acts as a **manager class**, which is responsible for keeping a collection of books and providing methods to add and display them. A manager class is not a special Python feature—it is a common object-oriented programming (OOP) design technique used to organize related objects and their behavior.

## Running
1.Install Python 3 on your computer.
2.Download or clone this repository.
3.Open a terminal in the project folder.
4.Run the script:
python main-library.py

On some systems, you may need to use:
python3 main-library.py



## My Submission Checklist

✓ Repository name and structure matches the assignment requirements.
✓ The README.md is complete and includes a project description, instructions, and any required information.
✓ The GitHub repository is public and accessible to anyone with the link and  opens correctly in a private/incognito browser window.
✓ each required files have been finished and pushed to GitHub.
✓ The project runs without errors.



## handling errors
if there's any error for example in letter case then the function lower() will fix it and enters it in small letters even if the user writes upper case letters or wrong case letters 
  Menu input is wrapped in try/except so entering letters instead of numbers does not crash the program.
  Book titles and author names are converted to lowercase using lower(), making searches case-insensitive.
  If the user tries to borrow or return a book that does not exist, a friendly message is displayed.
  The user can stop entering books by typing 0.
  If the author or publication year is unknown, - can be entered.
  The publication year is stored as a string because some books may have an unknown year.
  The menu keeps running until the user chooses to exit.





## update Features
 Borrow Book feature.
 Return Book feature.
Each Book object will be checked if available or not before change, and its status will be also checked
A book cannot be borrowed if it is already borrowed.
A returned book becomes available to borrow again and it can't be returned if it is available because this means that there is an error maybe it is not from our library
