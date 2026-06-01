class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        minimum = -1
        maximum = 0
        mode = 0
        mode_freq = 0

        total_count = 0
        total_sum = 0

        for i in range(256):
            if count[i] > 0:
                if minimum == -1:
                    minimum = i

                maximum = i
                total_count += count[i]
                total_sum += i * count[i]

                if count[i] > mode_freq:
                    mode_freq = count[i]
                    mode = i

        mean = float(total_sum) / total_count

        # Median
        if total_count % 2 == 1:
            target = total_count // 2 + 1
            curr = 0

            for i in range(256):
                curr += count[i]
                if curr >= target:
                    median = float(i)
                    break
        else:
            target1 = total_count // 2
            target2 = target1 + 1

            curr = 0
            m1 = m2 = 0

            for i in range(256):
                curr += count[i]

                if curr >= target1 and m1 == 0 and target1 > 0:
                    m1 = i

                if curr >= target2:
                    m2 = i
                    if m1 == 0 and target1 == 1:
                        m1 = i
                    break

            median = (m1 + m2) / 2.0

        return [float(minimum), float(maximum), mean, median, float(mode)]