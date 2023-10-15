from easyProblems import LeetcodeEasyProblems


def test_twoSum():
    nums = [2, 7, 11, 15]
    target = 9
    result = LeetcodeEasyProblems.twoSum(nums, target)
    assert result == [0, 1]


def test_isPalindrome():
    assert LeetcodeEasyProblems.isPalindrome(121) is True
    assert LeetcodeEasyProblems.isPalindrome(-121) is False


def test_romanToInt():
    assert LeetcodeEasyProblems.romanToInt("III") == 3
    assert LeetcodeEasyProblems.romanToInt("IV") == 4


def test_longestCommonPrefix():
    strs = ["flower", "flow", "flight"]
    result = LeetcodeEasyProblems.longestCommonPrefix(strs)
    assert result == "fl"


def test_validParenthesis():
    assert LeetcodeEasyProblems.validParenthesis("()[]{}") is True
    assert LeetcodeEasyProblems.validParenthesis("(]") is False


def test_removeDuplicates():
    nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
    result = LeetcodeEasyProblems.removeDuplicates(nums)
    assert result == 5
    assert nums[:result] == [1, 2, 3, 4, 5]


def test_removeElement():
    nums = [3, 2, 2, 3]
    val = 3
    result = LeetcodeEasyProblems.removeElement(nums, val)
    assert result == 2
    assert nums[:result] == [2, 2]


def test_climbStairs():
    assert LeetcodeEasyProblems.climbStairs(2) == 2
    assert LeetcodeEasyProblems.climbStairs(3) == 3


def test_plusOne():
    digits = [1, 2, 3]
    result = LeetcodeEasyProblems.plusOne(digits)
    assert result == [1, 2, 4]


def test_strStr():
    haystack = "hello"
    needle = "ll"
    result = LeetcodeEasyProblems.strStr(haystack, needle)
    assert result == 2


def test_searchInsert():
    nums = [1, 3, 5, 6]
    target = 5
    result = LeetcodeEasyProblems.searchInsert(nums, target)
    assert result == 2


def test_lengthOfLastWord():
    s = "Hello World"
    result = LeetcodeEasyProblems.lengthOfLastWord(s)
    assert result == 5


def test_reverseWords():
    s = "Let's code in Python"
    result = LeetcodeEasyProblems.reverseWords(s)
    assert result == "s'teL edoc ni nohtyP"
