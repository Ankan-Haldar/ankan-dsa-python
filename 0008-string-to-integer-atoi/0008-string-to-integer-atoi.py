class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)

        # Skip spaces
        while i < n and s[i] == " ":
            i += 1

        # Sign
        sign = 1
        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # Number
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # Clamp to 32-bit integer range
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num