# --- INITIAL DATA ---
# Setting up two groups of books for our library sections
science_books = {"Physics", "Chemistry", "Biology", "Maths"}
arts_books = {"History", "Literature", "Arts", "Maths"}

print(f"Science Section: {science_books}")
print(f"Arts Section: {arts_books}")

# --- 1. MATHEMATICAL OPERATIONS (Comparison) ---

# UNION: Let's combine everything to see the full collection of unique books
all_library_books = science_books.union(arts_books)
print(f"\n1. Union (All Collection): {all_library_books}")

# INTERSECTION: Finding out which books are common to both sections
common_books = science_books.intersection(arts_books)
print(f"2. Intersection (Shared Books): {common_books}")

# DIFFERENCE: Identifying books that belong only to Science and aren't in Arts
only_science = science_books.difference(arts_books)
print(f"3. Difference (Exclusive to Science): {only_science}")

# SYMMETRIC DIFFERENCE: Picking books that are in one section or the other, but not both
unique_to_each = science_books.symmetric_difference(arts_books)
print(f"4. Symmetric Difference (Unique items): {unique_to_each}")

# ISDISJOINT: Just checking if the two sections have absolutely nothing in common
is_separate = science_books.isdisjoint(arts_books)
print(f"5. Are the sets completely different? {is_separate}")


# --- 2. MODIFICATION FUNCTIONS (Editing) ---

# ADD: Putting a new single book into the Science set
science_books.add("Astronomy")
print(f"\n6. After adding a new book: {science_books}")

# UPDATE: Adding a bunch of new books all at once
science_books.update(["Robotics", "Genetics"])
print(f"7. After updating with multiple books: {science_books}")

# REMOVE: Deleting a specific book (this will throw an error if the book isn't found)
science_books.remove("Physics")
print(f"8. After removing Physics: {science_books}")

# DISCARD: A safer way to delete; it won't crash the program if the book is missing
science_books.discard("Non-Existent-Book")
print(f"9. After discarding (safe delete): {science_books}")

# POP: Removing a random item from the Arts set since sets don't have a fixed order
popped_book = arts_books.pop()
print(f"10. Randomly removed book: {popped_book} | Remaining Arts: {arts_books}")

# CLEAR: Wiping out the entire Arts set to start fresh
arts_books.clear()
print(f"11. After clearing the entire set: {arts_books}")