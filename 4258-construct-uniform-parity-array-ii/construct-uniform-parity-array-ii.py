class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # سب سے چھوٹا طاق (odd) نمبر ڈھونڈیں
        min_odd = None
        for x in nums1:
            if x % 2 != 0:
                if min_odd is None or x < min_odd:
                    min_odd = x
        
        # اگر کوئی طاق نمبر نہیں ہے تو جواب True ہے
        if min_odd is None:
            return True
            
        # اگر کوئی بھی ایون نمبر اس سب سے چھوٹے طاق نمبر سے چھوٹا نکلے تو False
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True
