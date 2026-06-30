class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = set()

        for src, dest in paths:
            sources.add(src)

        for src, dest in paths:
            if dest not in sources:
                return dest