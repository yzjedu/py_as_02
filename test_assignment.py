import unittest
from io import StringIO
import sys

class TestDaysInMonth(unittest.TestCase):

    def run_program_with_input(self, user_input):
        '''Runs the assignment.py program with the given input and returns the output.'''
        # Backup the original stdin and stdout
        original_stdin = sys.stdin
        original_stdout = sys.stdout

        # Redirect stdin and stdout
        sys.stdin = StringIO(user_input)
        sys.stdout = StringIO()

        # Run the script
        try:
            from assignment import main  # Import the main function
            main()  # Call the main function
            output = sys.stdout.getvalue()  # Capture the output
        finally:
            # Restore the original stdin and stdout
            sys.stdin = original_stdin
            sys.stdout = original_stdout

        return output.strip()

    def test_january_non_leap_year(self):
        output = self.run_program_with_input("1\n2021\n")
        self.assertIn("The month has 31 days", output)

    def test_february_leap_year(self):
        output = self.run_program_with_input("2\n2020\n")
        self.assertIn("The month has 29 days", output)

    def test_february_non_leap_year(self):
        output = self.run_program_with_input("2\n2021\n")
        self.assertIn("The month has 28 days", output)

    def test_april(self):
        output = self.run_program_with_input("4\n2021\n")
        self.assertIn("The month has 30 days", output)

    def test_invalid_month(self):
        output = self.run_program_with_input("13\n2021\n")
        self.assertIn("Invalid month", output)

if __name__ == "__main__":
    unittest.main()
