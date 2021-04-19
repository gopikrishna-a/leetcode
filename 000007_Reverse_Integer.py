class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = ""
        for i in str(x):
            s = i + s
        if "-" in s:
            s = s.strip("-")
            s = "-" + s
        if int(s) < -2 ** 31 or int(s) > 2 ** 31:
            return 0

        
        return int(s)
