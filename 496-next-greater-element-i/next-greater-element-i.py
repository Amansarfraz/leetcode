class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}  # map: number -> next greater
        
        # 🔥 process nums2
        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)
        
        # remaining elements have no greater
        for num in stack:
            nge[num] = -1
        
        # build result for nums1
        return [nge[num] for num in nums1]