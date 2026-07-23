# Topic 14 Collaborative Assignment
# Your Name: Bradley Moore
# Date: 22 July 2026

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

class Magazine(LibraryItem):
    """A magazine in the library catalog."""
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self.issue_number = issue_number

    def describe(self):
        return f"{self.title}, Issue {self.issue_number} ({self.year})"

    def item_type(self):
        return "Magazine"

class DVD(LibraryItem):
    """A DVD in the library catalog."""
    def __init__(self, title, year, duration_minutes):
        super().__init__(title, year)
        self.duration_minutes = duration_minutes

    def describe(self):
        return f"{self.title} ({self.year}) - {self.duration_minutes} min"

    def item_type(self):
        return "DVD"


# Create new items
mag1 = Magazine("Python Monthly", 2024, "07")
dvd1 = DVD("Inception", 2010, 148)

# Add them to the catalog
catalog.append(mag1)
catalog.append(dvd1)


print("\n--- Full Catalog ---")
for item in catalog:
    print(item.describe())
    print("Type:", item.item_type())


print("Items in catalog:", count_items(catalog))
