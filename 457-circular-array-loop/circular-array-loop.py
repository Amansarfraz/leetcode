class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow, fast = i, i

            while True:
                # move slow one step
                slow_next = next_index(slow)
                if nums[slow_next] == 0 or (nums[slow_next] > 0) != direction:
                    break

                # move fast one step
                fast_next = next_index(fast)
                if nums[fast_next] == 0 or (nums[fast_next] > 0) != direction:
                    break

                # move fast second step
                fast_next2 = next_index(fast_next)
                if nums[fast_next2] == 0 or (nums[fast_next2] > 0) != direction:
                    break

                slow = slow_next
                fast = fast_next2

                if slow == fast:
                    if slow == next_index(slow):  # self loop
                        break
                    return True

            # mark visited
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False