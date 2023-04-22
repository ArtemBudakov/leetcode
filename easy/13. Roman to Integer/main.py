class Solution:
    def romanToInt(self, s: str) -> int:
        """
            I can be placed before V (5) and X (10) to make 4 and 9.
            X can be placed before L (50) and C (100) to make 40 and 90.
            C can be placed before D (500) and M (1000) to make 400 and 900.
        """

        alphabet = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if len(s) == 1:
            return alphabet[s]

        result: int = 0
        previous_digit: int = 0
        for digit in s:
            # full case
            if previous_digit == 0:
                previous_digit = alphabet[digit]
                continue

            if previous_digit < alphabet[digit]:
                result += alphabet[digit] - previous_digit
                previous_digit = 0
            else:
                result += previous_digit
                previous_digit = alphabet[digit]
        else:
            result += previous_digit

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("LVIII"))  # 58
    print(sol.romanToInt("IX"))  # 9
    print(sol.romanToInt("MCMXCIV"))  # 1994
