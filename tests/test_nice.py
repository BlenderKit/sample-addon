import unittest
import sys
from io import StringIO

from sample_addon import nice

class TestFunctions(unittest.TestCase):
    def setUp(self):
        # Redirect the print output to a StringIO object
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset the redirection of sys.stdout
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_hello(self):
        nice.hello()
        self.held_output.seek(0)  # Go to the beginning of the StringIO buffer
        output = self.held_output.read().strip()  # Read the content and remove any trailing whitespaces
        self.assertEqual(output, "Hello!")

    def test_goodbye(self):
        nice.goodbye()
        self.held_output.seek(0)  # Go to the beginning of the StringIO buffer
        output = self.held_output.read().strip()  # Read the content and remove any trailing whitespaces
        self.assertEqual(output, "Goodbye!")
