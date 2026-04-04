class Node(object):
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne(object):

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.key_map = {}  # key -> node

    # 🔧 helper: insert node after prev
    def _add_node(self, prev, node):
        node.next = prev.next
        node.prev = prev
        prev.next.prev = node
        prev.next = node

    # 🔧 helper: remove node
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key in self.key_map:
            curr = self.key_map[key]
            nxt = curr.next
            
            # move to next count
            if nxt == self.tail or nxt.count != curr.count + 1:
                new_node = Node(curr.count + 1)
                self._add_node(curr, new_node)
                nxt = new_node
            
            nxt.keys.add(key)
            self.key_map[key] = nxt
            
            curr.keys.remove(key)
            if not curr.keys:
                self._remove_node(curr)
        else:
            # new key → count = 1
            if self.head.next == self.tail or self.head.next.count != 1:
                new_node = Node(1)
                self._add_node(self.head, new_node)
            
            self.head.next.keys.add(key)
            self.key_map[key] = self.head.next

    def dec(self, key):
        if key not in self.key_map:
            return
        
        curr = self.key_map[key]
        
        if curr.count == 1:
            # remove key completely
            del self.key_map[key]
        else:
            prev = curr.prev
            
            if prev == self.head or prev.count != curr.count - 1:
                new_node = Node(curr.count - 1)
                self._add_node(curr.prev, new_node)
                prev = new_node
            
            prev.keys.add(key)
            self.key_map[key] = prev
        
        curr.keys.remove(key)
        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))