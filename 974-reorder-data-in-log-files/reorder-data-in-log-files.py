class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            identifier, content = log.split(" ", 1)
            
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((content, identifier, log))
        
        letter_logs.sort()
        
        return [log for _, _, log in letter_logs] + digit_logs