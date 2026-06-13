from collections import defaultdict, deque

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        # Assign unique groups to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indegree[v] += 1

                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        def topo(nodes, graph, indegree):
            q = deque()

            for node in nodes:
                if indegree[node] == 0:
                    q.append(node)

            order = []

            while q:
                cur = q.popleft()
                order.append(cur)

                for nxt in graph[cur]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        q.append(nxt)

            return order if len(order) == len(nodes) else []

        item_order = topo(range(n), item_graph, item_indegree[:])
        if not item_order:
            return []

        group_order = topo(range(m), group_graph, group_indegree[:])
        if not group_order:
            return []

        group_items = defaultdict(list)

        for item in item_order:
            group_items[group[item]].append(item)

        result = []

        for g in group_order:
            result.extend(group_items[g])

        return result