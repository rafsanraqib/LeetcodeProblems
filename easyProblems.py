"""
This class provides a collection of methods for various coding problems 
gathered from leetcode of the easy difficulty.

"""


class LeetcodeEasyProblems:
    # Function to find two numbers in the 'nums' list that add up to 'target'
    # Time Complexity: O(n^2) where 'n' is the length of 'nums'
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Function to check if a given integer 'x' is a palindrome
    # Time Complexity: O(log(x)) since we are converting 'x' to a string
    def isPalindrome(x):
        if x % 10 == 0 and x != 0:
            return False
        str_x = str(x)
        str_x_len = len(str_x)
        str_x_mid = int(str_x_len / 2)
        for i in range(str_x_mid):
            if str_x[i] != str_x[str_x_len - i - 1]:
                return False
        return True

    # Function to convert a Roman numeral 's' to an integer
    # Time Complexity: O(n) where 'n' is the length of the input string 's'
    def romanToInt(s):
        roman_numbers = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000, "IV": 4,
            "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }
        integer_version = 0
        i = 0
        while i < len(s):
            if i + 1 != len(s) and s[i] + s[i + 1] in roman_numbers.keys():
                integer_version += roman_numbers[s[i] + s[i + 1]]
                i += 2
                continue
            integer_version += roman_numbers[s[i]]
            i += 1
        return integer_version

    # Function to find the longest common prefix among a list of strings 'strs'
    # Time Complexity: O(m*n) in the worst case, where 'm' is the length of the shortest string and 'n' is the number of strings
    def longestCommonPrefix(strs):
        common_prefix = ""
        minimum_length = min(len(s) for s in strs)
        for i in range(minimum_length):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if temp != strs[j][i]:
                    return common_prefix
            common_prefix += temp
        return common_prefix

    # Function to check the validity of a string containing parentheses 's'
    # Time Complexity: O(n) where 'n' is the length of the input string 's'
    def validParenthesis(s):
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "{":
                stack.append("}")
            elif s[i] == "[":
                stack.append("]")
            elif s[i] == "(":
                stack.append(")")
            elif len(stack) == 0 or s[i] != stack.pop():
                return False
        return len(stack) == 0

    # Function to remove duplicate elements from the 'nums' list and return the new length
    # Time Complexity: O(n) where 'n' is the length of 'nums'
    def removeDuplicates(nums):
        if not nums:
            return 0
        dict = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] in dict.keys():
                dict[nums[i]] += 1
                continue
            dict[nums[i]] = 1
            k += 1
        index = 0
        for key in dict.keys():
            nums[index] = key
            index += 1
        return k

    # Function to remove all occurrences of 'val' from the 'nums' list and return the new length
    # Time Complexity: O(n) where 'n' is the length of 'nums'
    def removeElement(nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    # Function to find the number of distinct ways to climb 'n' stairs
    # Time Complexity: O(n)
    def climbStairs(n):
        steps_list = [1, 2]
        if n == 1 or n == 2:
            return steps_list[n - 1]
        steps = 0
        for i in range(3, n):
            steps = steps_list[0] + steps_list[1]
            steps_list[0] = steps_list[1]
            steps_list[1] = steps
        return steps_list[0] + steps_list[1]

    # Function to add one to a list of digits 'digits' representing a non-negative integer
    # Time Complexity: O(n) where 'n' is the length of 'digits'
    def plusOne(digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry <= 0:
                return digits
            digits[i] += carry
            carry = digits[i] - 9
            if digits[i] > 9:
                digits[i] = 0
        if carry > 0:
            digits = [carry] + digits
        return digits

    # Function to find the index of the first occurrence of 'needle' in 'haystack'
    # Time Complexity: O(m*n) in the worst case, where 'm' is the length of 'haystack' and 'n' is the length of 'needle'
    def strStr(haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    # Function to find the index where 'target' should be inserted into the sorted 'nums' list
    # Time Complexity: O(log(n)) where 'n' is the length of 'nums'
    def searchInsert(nums, target):
        mid_point = int(len(nums) / 2)
        start = 0
        end = 0
        if nums[mid_point] > target:
            start = 0
            end = mid_point + 1
        elif nums[mid_point] < target:
            start = mid_point
            end = len(nums)
        elif nums[mid_point] == target:
            return mid_point
        for i in range(start, end):
            if nums[i] == target or nums[i] > target:
                return i
        return len(nums)

    # Function to calculate the length of the last word in a string
    def lengthOfLastWord(s):
        lst = s.rstrip().split(" ")
        return len(lst[-1])

    # Function to reverse the order of words in a string
    def reverseWords(s):
        lst = s.split(" ")
        final_str = ""

        for i in range(len(lst) - 1):
            final_str += lst[i][::-1] + " "

        final_str += lst[-1][::-1]
        return final_str
