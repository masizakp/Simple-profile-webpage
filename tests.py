from django.test import TestCase

class SimpleTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_uppercase(self):
        self.assertEqual("hello".upper(), "HELLO")
