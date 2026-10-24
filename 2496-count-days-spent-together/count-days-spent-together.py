class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str):
            # Parse "MM-DD" into integers
            month, day = map(int, date_str.split('-'))
            # Sum the days of all preceding months plus the current month's days
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all MM-DD dates to absolute day numbers (1 to 365)
        start_alice = date_to_day_of_year(arriveAlice)
        end_alice = date_to_day_of_year(leaveAlice)
        start_bob = date_to_day_of_year(arriveBob)
        end_bob = date_to_day_of_year(leaveBob)
        
        # Find the intersection of both intervals
        overlap_start = max(start_alice, start_bob)
        overlap_end = min(end_alice, end_bob)
        
        # Calculate overlap length
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        return 0
