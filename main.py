class Solution:
    def reverse(x: int) -> int:
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Check if the number is negative
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits of the integter
        reversed_x = 0
        while x:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Restore the sign
        reversed_x *= sign

        # Check if the reversed integer is within the 32-bit signed integer range
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        return reversed_x