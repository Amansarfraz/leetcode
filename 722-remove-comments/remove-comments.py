class Solution(object):
    def removeComments(self, source):
        in_block = False
        res = []
        new_line = []

        for line in source:
            i = 0
            if not in_block:
                new_line = []

            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
                    in_block = False
                    i += 2
                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
                    break
                else:
                    if not in_block:
                        new_line.append(line[i])
                    i += 1

            if not in_block and new_line:
                res.append("".join(new_line))

        return res