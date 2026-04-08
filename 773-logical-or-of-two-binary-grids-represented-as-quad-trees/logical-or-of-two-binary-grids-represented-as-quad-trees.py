class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        # Case 1: if quadTree1 is leaf
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        
        # Case 2: if quadTree2 is leaf
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        
        # Case 3: both are non-leaf → recurse
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # Case 4: merge if possible
        if (topLeft.isLeaf and topRight.isLeaf and 
            bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            
            return Node(topLeft.val, True, None, None, None, None)
        
        # otherwise return internal node
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)