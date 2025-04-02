import unittest
class Solve:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Check if the number is negative
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits of the integter
        reversed_x = 0
        while x:
            digit = x % 10
            # Check if the reversed integer is within the 32-bit signed integer range
            if reversed_x > (INT_MIN // 10) or (reversed_x == (INT_MAX // 10) and digit > INT_MAX % 10):
                return 0
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Restore the sign
        return reversed_x * sign

class TestSolve(unittest.TestCase):
    def setUp(self):
        self.solver = Solve()

    def test_reverse_positive(self):
        self.assertEqual(self.solver.reverse(123), 321)

    def test_reverse_negative(self):
        self.assertEqual(self.solver.reverse(-123), -321)

    def test_reverse_zero(self):
        self.assertEqual(self.solver.reverse(0), 0)

    def test_reverse_with_trailing_zeros(self):
        self.assertEqual(self.solver.reverse(120), 21)

    def test_reverse_large_number(self):
        self.assertEqual(self.solver.reverse(1534236469), 0)  # Overflow case

if __name__ == "__main__":
    unittest.main()