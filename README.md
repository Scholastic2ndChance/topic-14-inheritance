# Topic 14: Inheritance and Recursion

**Week 7 | CIS Intro to Programming**

---

## Overview

This is the final collaborative assignment. This week focuses on inheritance — one of the most important concepts in object-oriented programming. A small recursive function is already provided in `starter.py`, but your main task is to extend the inheritance structure. Read the existing code carefully before you begin.

## Assignment Prompt

The starter code in `starter.py` defines a base class and one subclass, and includes a small recursive helper function already implemented for you. Your task is to extend the program by:

- Adding at least one new subclass that inherits from the base class
- Overriding at least one method in your new subclass to give it different behavior
- Creating instances of at least two different subclasses and demonstrating that the same method call behaves differently depending on the object (polymorphism)
- Leaving the recursive function as-is — you do not need to modify it, but your peer review discussion this week can include observations about how it works

The theme is a simple library catalog. Read the existing code, then extend it in whatever direction makes sense to you.

## Starter Code

The starter code is provided in `starter.py` in this repository. Copy it into your fork as your starting point and add your new subclass(es) below the existing code.

```python
# Topic 14 Collaborative Assignment
# Your Name:
# Date:

# --- PROVIDED CODE: Do not modify this section ---

class LibraryItem:
    """Base class for all items in the library catalog."""
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe(self):
        return f"{self.title} ({self.year})"

    def item_type(self):
        return "Library Item"


class Book(LibraryItem):
    """A book in the library catalog."""
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author} ({self.year})"

    def item_type(self):
        return "Book"


def count_items(catalog, index=0):
    """Recursively count items in a catalog list."""
    if index == len(catalog):
        return 0
    return 1 + count_items(catalog, index + 1)


# --- Sample usage of provided code ---
book1 = Book("The Pragmatic Programmer", 1999, "Hunt & Thomas")
print(book1.describe())
print("Type:", book1.item_type())

catalog = [book1]
print("Items in catalog:", count_items(catalog))

# --- YOUR CODE BELOW THIS LINE ---
# Add at least one new subclass (e.g., Magazine, DVD, Audiobook, Journal)
# Override describe() and item_type() in your subclass
# Create instances of your new subclass and add them to the catalog
# Call count_items(catalog) again to show the updated count
```

## Peer Review Prompt

When reviewing a classmate's code this week, consider:

- Does their new subclass make sense as a type of library item?
- Did they override the methods in a way that feels natural and different from the base class?
- Can you see the polymorphism working — i.e., does the same method call produce different output depending on the object?
- As a bonus: can you trace through the `count_items` recursive function in your head and explain how it works in your Issue?

## Submission Instructions

1. Fork this repository into your own GitHub account.
2. Copy `starter.py` into your fork and add your code below the provided section.
3. Commit your completed file.
4. Submit your repo link using the **Submit Your Repo Link** form in Blackboard.
5. Open the **Class Repo Directory** in Blackboard and find two classmates' repos.
6. Leave a GitHub Issue on each with substantive feedback using the peer review prompt above as your guide.

## Notes

This is the last assignment of the semester. Take a moment to compare how much more complex this program is than your Week 1 submission — that growth is real. Strong peer feedback this week might include observations about the recursive function for classmates who want to discuss it.
