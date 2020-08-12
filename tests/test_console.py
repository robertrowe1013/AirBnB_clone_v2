#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch

class TestConsole(unittest.TestCase)
    def test_console(self):
        """ test console """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create bad")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")
