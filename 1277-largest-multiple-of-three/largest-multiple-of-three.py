class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        digits.sort()
        total = sum(digits)

        rem1 = []
        rem2 = []

        for i, d in enumerate(digits):
            if d % 3 == 1:
                rem1.append(i)
            elif d % 3 == 2:
                rem2.append(i)

        remove = set()

        r = total % 3

        if r == 1:
            if rem1:
                remove.add(rem1[0])
            elif len(rem2) >= 2:
                remove.add(rem2[0])
                remove.add(rem2[1])
            else:
                return ""
        elif r == 2:
            if rem2:
                remove.add(rem2[0])
            elif len(rem1) >= 2:
                remove.add(rem1[0])
                remove.add(rem1[1])
            else:
                return ""

        res = [str(digits[i]) for i in range(len(digits)) if i not in remove]

        if not res:
            return ""

        res.sort(reverse=True)

        if res[0] == '0':
            return "0"

        return "".join(res)