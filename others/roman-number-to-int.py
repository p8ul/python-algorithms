"""
https://leetcode.com/problems/roman-to-integer/submissions/
written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""


def roman_to_int(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = []
    for i in s:
        res.append(roman[i])
    ans = 0
    visited = []
    for i in range(0, len(res)):
        if i in visited:
            continue
        _next = 0 if i + 1 == len(res) else res[i + 1]
        current = res[i]
        if _next > current:
            ans += _next - current
            if _next != 0:
                visited.append(i + 1)
        else:
            ans += current
    return ans


if __name__ == '__main__':
    print(roman_to_int("MCMXCIV"))  # 1994
