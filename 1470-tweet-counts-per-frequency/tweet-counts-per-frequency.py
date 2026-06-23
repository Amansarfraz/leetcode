from collections import defaultdict
import bisect

class TweetCounts(object):

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        interval = {
            "minute": 60,
            "hour": 3600,
            "day": 86400
        }[freq]

        size = (endTime - startTime) // interval + 1
        result = [0] * size

        times = self.tweets[tweetName]

        left = bisect.bisect_left(times, startTime)
        right = bisect.bisect_right(times, endTime)

        for t in times[left:right]:
            idx = (t - startTime) // interval
            result[idx] += 1

        return result