class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        curr = 1

        for num in target:
            while curr < num:
                ans.append("Push")
                ans.append("Pop")
                curr += 1

            ans.append("Push")
            curr += 1

        return ans