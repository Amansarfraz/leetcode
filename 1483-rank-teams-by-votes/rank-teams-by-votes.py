class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        teams = votes[0]
        n = len(teams)

        count = {team: [0] * n for team in teams}

        for vote in votes:
            for pos, team in enumerate(vote):
                count[team][pos] += 1

        teams = list(teams)

        teams.sort(key=lambda t: ([-count[t][i] for i in range(n)], t))

        return "".join(teams)