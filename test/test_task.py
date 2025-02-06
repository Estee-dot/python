import unittest
from classTask import char_task as task

class TestTask(unittest.TestCase):
    def test_that_encrypt_text_exist(self):
        task.encrypt_text("hello")

    def test_that_encrypt_text_returns_correct_value(self):
        actual = task.encrypt_text("Hello, World!")
        expected = "Uryyb, Jbeyq!"
        self.assertEqual(actual, expected)
        actual = task.encrypt_text("Welcome, 123")
        expected = "Jrypbzr, 123"
        self.assertEqual(actual, expected)

    def test_that_encrypt_text_raise_exception_with_invalid_input(self):
        self.assertRaises(TypeError, task.encrypt_text, 123)

    def test_that_encrypt_text_leaves_Non_Alphabet_characters_unchanged(self):
        actual = task.encrypt_text("Hello12, World!")
        expected = "Uryyb12, Jbeyq!"
        self.assertEqual(actual, expected)

    def test_that_encrypt_text_is_case_insensitive(self):
        actual = task.encrypt_text("HELLO")
        expected = "URYYB"
        self.assertEqual(actual, expected)


