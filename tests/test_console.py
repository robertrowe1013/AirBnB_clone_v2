#!/usr/bin/python3
""" test console """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ test console """
    def test_console(self):
        """ test console """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create bad")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
