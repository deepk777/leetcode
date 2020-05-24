# Counting element
# Given an integer array, count element x such that x + 1 is also in array.If there're duplicates in array, count them separately.

#    Example 1:
#         Input: {1, 2, 3}
#         Output: 2
#            Explanation:
#             First element is 1 + 1 = 2 (2 is present in an array)
#             Second element is 2 + 1 = 3 (3 is present in an array)
#             Third element is 3 + 1 = 4 (4 is not present in an array)
#
#     Example 2:
#         Input: {1, 1, 3, 3, 5, 5, 7, 7}
#         Output: 0
#
#     Example 3:
#         Input: {1, 3, 2, 3, 5, 0}
#         Output: 3
#         Explanation:
#             1 + 1 = 2 (Exist)
#             3 + 1 = 4 (Not exist)
#             2 + 1 = 3 (Exist)
#             3 + 1 = 4 (Not exist)
#             5 + 1 = 6 (Not exist)
#             0 + 1 = 1 (Exist)
#
#     Example 4:
#       Input: {1, 1, 2, 2}
#       Output: 2


from collections import defaultdict


class Solution(object):
    def countElements(self, arr):

        number_dictionary = defaultdict(int)
        count = 0

        for num in arr:
            number_dictionary[num] += 1

        for num in number_dictionary:
            count += number_dictionary.get(num-1, 0)

        return count
