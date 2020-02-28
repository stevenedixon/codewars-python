# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
# starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and
# 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in
# descending order.
#
# Example:
#
# solution('XXI') # should return 21
#
# Help:
#
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000


def solution(roman):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for i in range(len(roman)):
        if i > 0 and symbols[roman[i]] > symbols[roman[i - 1]]:
            value += symbols[roman[i]] - 2 * symbols[roman[i - 1]]
        else:
            value += symbols[roman[i]]
    return value


# Basic Tests
print(solution('XXI'))  # 21
print(solution('I'))  # 1
print(solution('IV'))  # 4
print(solution('MMVIII'))  # 2008
print(solution('MDCLXVI'))  # 1666
