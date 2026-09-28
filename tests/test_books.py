import tempfile, os
import unittest
from unittest.mock import patch

class TestBookValidation(unittest.TestCase):
    def test_positive_copies(self):
        from validation import positive_int
        self.assertEqual(positive_int("3", "Copies"), 3)

    def test_invalid_copies(self):
        from validation import positive_int
        with self.assertRaises(ValueError):
            positive_int("0", "Copies")

if __name__ == "__main__":
    unittest.main()
