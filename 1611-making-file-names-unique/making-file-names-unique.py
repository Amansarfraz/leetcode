class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        used = {}
        ans = []

        for name in names:
            if name not in used:
                ans.append(name)
                used[name] = 1
            else:
                k = used[name]
                while "{}({})".format(name, k) in used:
                    k += 1
                new_name = "{}({})".format(name, k)
                ans.append(new_name)
                used[name] = k + 1
                used[new_name] = 1

        return ans