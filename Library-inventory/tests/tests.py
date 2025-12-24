import unittest
from library_manager.book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        b = Book("gaming basics", "Trijal", "98769")
        self.assertEqual(b.title, "GAming basics")
        self.assertEqual(b.status, "available")

    def test_issue_return(self):
        b = Book("Test Book", "Author", "999")
        # Test Issue
        self.assertTrue(b.issue())
        self.assertEqual(b.status, "issued")
        # Test Issue again (should fail)
        self.assertFalse(b.issue())
        # Test Return
        b.return_book()
        self.assertEqual(b.status, "available")

if __name__ == '__main__':
    unittest.main()