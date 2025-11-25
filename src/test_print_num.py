import unittest
from io import StringIO
import sys
from print_num import print_num

class TestPrintNum(unittest.TestCase):
    
    def capture_output(self, func, *args):
        """Helper function to capture printed output"""
        captured_output = StringIO()
        sys.stdout = captured_output
        func(*args)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()
    
    def test_print_num_10(self):
        """Test printing numbers from 1 to 10"""
        output = self.capture_output(print_num, 10)
        expected = "".join(f"{i}\n" for i in range(1, 11))
        self.assertEqual(output, expected)
    
    def test_print_num_5(self):
        """Test printing numbers from 1 to 5"""
        output = self.capture_output(print_num, 5)
        expected = "".join(f"{i}\n" for i in range(1, 6))
        self.assertEqual(output, expected)
    
    def test_print_num_1(self):
        """Test printing only number 1"""
        output = self.capture_output(print_num, 1)
        self.assertEqual(output, "1\n")
    
    def test_print_num_0(self):
        """Test printing with 0 (should print nothing)"""
        output = self.capture_output(print_num, 0)
        self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()