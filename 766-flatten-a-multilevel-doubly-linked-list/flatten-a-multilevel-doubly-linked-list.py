class Solution(object):
    def flatten(self, head):
        
        def dfs(node):
            curr = node
            last = None
            
            while curr:
                nxt = curr.next
                
                # If child exists → flatten it
                if curr.child:
                    child_head = curr.child
                    child_tail = dfs(child_head)
                    
                    # connect curr with child
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None
                    
                    # connect child tail with nxt
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail
                    
                    last = child_tail
                    curr = child_tail
                else:
                    last = curr
                
                curr = curr.next
            
            return last
        
        dfs(head)
        return head