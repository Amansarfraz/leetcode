class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        ans = 0

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                total = arr[i] + arr[j] + arr[k]

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    if arr[j] == arr[k]:
                        count = k - j + 1
                        ans += count * (count - 1) // 2
                        ans %= MOD
                        break
                    else:
                        left = 1
                        right = 1

                        while j + 1 < k and arr[j] == arr[j + 1]:
                            left += 1
                            j += 1

                        while k - 1 > j and arr[k] == arr[k - 1]:
                            right += 1
                            k -= 1

                        ans += left * right
                        ans %= MOD

                        j += 1
                        k -= 1

        return ans % MOD