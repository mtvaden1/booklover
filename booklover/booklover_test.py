import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        testValue = test_object.book_list['book_name'].unique().__contains__("War of the Worlds")

        message=("Test 1 failed")

        self.assertTrue(testValue, message)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)

        testValue= test_object.num_books
        
        message=("Test 2 failed")
        
        expected = 1
        
        self.assertEqual(testValue, expected, message)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        testValue = test_object.has_read("War of the Worlds")

        message=("Test 3 failed")

        self.assertTrue(testValue, message)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        testValue = test_object.has_read("Percy Jackson")

        message=("Test 4 failed")

        self.assertFalse(testValue, message)

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("The Pillars of the Earth", 4)
        test_object.add_book("The Hunger Games", 5)
        testValue= test_object.num_books_read()

        expected = 3

        message=("Test 5 failed")

        self.assertEqual(testValue, expected, message)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("The Pillars of the Earth", 4)
        test_object.add_book("The Hunger Games", 5)
        test_object.add_book("Bad Book", 1)

        testValue= test_object.fav_books().query("book_rating > 3").shape[0]

        expected = 3

        message=("Test 6 failed")

        self.assertEqual(testValue, expected, message)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)