class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            folder = parts[0]

            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1]  # remove ')'

                full_path = folder + '/' + name
                content_map[content].append(full_path)

        result = []

        for files in content_map.values():
            if len(files) > 1:
                result.append(files)

        return result