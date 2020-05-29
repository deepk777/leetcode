# Counting Bits
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
# Input: 2
# Output: [0, 1, 1]
#
# Example 2:
# Input: 5
# Output: [0, 1, 1, 2, 1, 2]
# Follow up:
#
# Space complexity should be O(n).


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        ans = []
        store = dict()
        ans.append(0)
        store[0] = 0
        for i in range(1, num+1):
            count = 0
            n = i
            while i:
                if store.get(i):
                    count += store.get(i)
                    break
                if i & 1:
                    count += 1
                i = i >> 1
            store[n] = count
            ans.append(count)

        return ans
