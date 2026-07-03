class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        sets = [set(companies) for companies in favoriteCompanies]
        ans = []

        for i in range(len(sets)):
            is_subset = False
            for j in range(len(sets)):
                if i != j and len(sets[i]) <= len(sets[j]):
                    if sets[i].issubset(sets[j]):
                        is_subset = True
                        break
            if not is_subset:
                ans.append(i)

        return ans