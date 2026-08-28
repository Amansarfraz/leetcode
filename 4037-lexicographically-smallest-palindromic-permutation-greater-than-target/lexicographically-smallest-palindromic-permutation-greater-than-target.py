class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        # Count characters
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether palindrome is possible
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                if middle != "":
                    return ""

                middle = chr(ord('a') + i)
                count[i] -= 1

        # count now contains even frequencies
        # We will work with the left half.
        #
        # For every character in target's left half,
        # remove two copies because palindrome needs
        # one copy on each side.
        half = n // 2

        for i in range(half):
            ch = target[i]
            count[ord(ch) - ord('a')] -= 2

        # -------------------------------------------------
        # Case 1:
        # The left half can be exactly the same as target's
        # left half.
        #
        # Then check whether its palindrome is already
        # greater than target.
        # -------------------------------------------------

        possible = True

        for c in count:
            if c < 0:
                possible = False
                break

        if possible:
            left = target[:half]

            # Construct palindrome using target's left half
            right = middle + left[::-1]

            candidate = left + right

            if candidate > target:
                return candidate

        # -------------------------------------------------
        # Case 2:
        # We need to make the left half slightly bigger.
        #
        # Start from the right side of target's left half
        # and try to increase one character.
        # -------------------------------------------------

        for i in range(half - 1, -1, -1):

            ch_index = ord(target[i]) - ord('a')

            # Restore the two copies used by target[i]
            count[ch_index] += 2

            # Check if target[:i] can still be formed
            possible = True

            for c in count:
                if c < 0:
                    possible = False
                    break

            if not possible:
                continue

            # Try the smallest character greater than target[i]
            for new_index in range(ch_index + 1, 26):

                # Need two copies for the palindrome
                if count[new_index] < 2:
                    continue

                # Use these two copies
                count[new_index] -= 2

                # Build the left half
                left = list(target[:i + 1])

                # Increase current character
                left[i] = chr(ord('a') + new_index)

                # Fill remaining positions with smallest
                # possible characters to get lexicographically
                # smallest answer.
                for k in range(26):
                    if count[k] > 0:
                        left.append(
                            chr(ord('a') + k) * (count[k] // 2)
                        )

                left = ''.join(left)

                # Mirror the left half
                right = left[::-1]

                # Construct complete palindrome
                answer = left + middle + right

                return answer

        # No valid palindrome greater than target
        return ""