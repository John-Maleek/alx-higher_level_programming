#!/usr/bin/python3
"""A test module for Rectangle class implementation"""


import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines test class"""
    def test_pep8_base(self):
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/rectangle.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_rectangle_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')

    def test_type_param(self):
        with self.assertRaises(TypeError):
            Rectangle(1.01, 3)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(-234234242, 45)
            raise ValueError()

        with self.assertRaises(TypeError):
            Rectangle('', 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(True, 4)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 1.76)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, "Hello")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, False)
            raise TypeError()

        with self.assertRaises(ValueError):
            Rectangle(5, -4798576398576)
            raise ValueError

        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 6, "test")
            raise TypeError()

        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)
            raise TypeError()
