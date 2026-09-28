import unittest

class TestMemberValidation(unittest.TestCase):
    def test_valid_email(self):
        from validation import email
        self.assertEqual(email("student@example.com"), "student@example.com")

    def test_invalid_email(self):
        from validation import email
        with self.assertRaises(ValueError):
            email("invalid-email")

if __name__ == "__main__":
    unittest.main()
