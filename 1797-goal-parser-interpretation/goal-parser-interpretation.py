class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        # Replace "()" with "o" first, then replace "(al)" with "al"
        return command.replace("()", "o").replace("(al)", "al")
