class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        n = len(req_skills)
        skill_id = {skill: i for i, skill in enumerate(req_skills)}

        people_masks = []
        for person in people:
            mask = 0
            for skill in person:
                if skill in skill_id:
                    mask |= 1 << skill_id[skill]
            people_masks.append(mask)

        dp = {0: []}  # mask -> team

        for i, p_mask in enumerate(people_masks):
            for mask, team in list(dp.items()):
                new_mask = mask | p_mask

                if new_mask == mask:
                    continue

                if (new_mask not in dp or
                        len(dp[new_mask]) > len(team) + 1):
                    dp[new_mask] = team + [i]

        return dp[(1 << n) - 1]