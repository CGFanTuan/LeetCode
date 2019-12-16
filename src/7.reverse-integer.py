#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev_num = 0
        if x == 0:
            return 0
        flg = x/abs(x)
        x = abs(x)
        while x != 0 :
            rev_num = rev_num*10 + x%10
            x = x/10
        rev_num = rev_num*flg
        if rev_num<-2147483648 or rev_num > 2147483647:
            return 0
        return rev_num
# @lc code=end

