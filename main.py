<<<<<<< HEAD
import unittest

=======
>>>>>>> origin/main
class Solve:
    def reverse(self, x: int) -> int:        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = 0
        while x:
            digit = x % 10
<<<<<<< HEAD
            if reversed_x > (INT_MIN // 10) or (reversed_x == (INT_MAX // 10) and digit > INT_MAX % 10):
=======
            # Check if the reversed integer is within the 32-bit signed integer range
            if reversed_x > (INT_MAX // 10) or (reversed_x == (INT_MAX // 10) and digit > INT_MAX % 10):
>>>>>>> origin/main
                return 0
            reversed_x = reversed_x * 10 + digit
            x //= 10

        return reversed_x * sign

<<<<<<< HEAD
class TestSolve(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solver = Solve()
=======
# Apply Usage
solver = Solve()
>>>>>>> origin/main

# Test cases
print(solver.reverse(123))
print(solver.reverse(-123))
print(solver.reverse(120))
print(solver.reverse(0))