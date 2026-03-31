class Solution(object):
    def readBinaryWatch(self, turnedOn):
        def count_bits(x):
            return bin(x).count('1')

        result = []

        for hour in range(12):
            for minute in range(60):
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    result.append("%d:%02d" % (hour, minute))

        return result