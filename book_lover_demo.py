from booklover import booklover
import pandas as pd

test = booklover.BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
test.add_book("War of the Worlds", 4)

print("The number of books in your list is: ", test.num_books)