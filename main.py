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
            if reversed_x > (INT_MAX // 10) or (reversed_x == (INT_MAX // 10) and digit > INT_MAX % 10):
                return 0
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Restore the sign
        return reversed_x * sign

# Apply Usage
solver = Solve()

# Test cases
print(solver.reverse(123))
print(solver.reverse(-123))
print(solver.reverse(120))
print(solver.reverse(0))