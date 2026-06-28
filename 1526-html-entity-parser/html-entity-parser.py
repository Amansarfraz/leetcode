class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        entities = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        ans = []
        i = 0

        while i < len(text):
            found = False

            for entity, ch in entities.items():
                if text.startswith(entity, i):
                    ans.append(ch)
                    i += len(entity)
                    found = True
                    break

            if not found:
                ans.append(text[i])
                i += 1

        return "".join(ans)