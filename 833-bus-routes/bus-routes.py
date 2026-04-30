from collections import defaultdict, deque

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        # Map stop -> buses
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(i)
        
        visited_stops = set([source])
        used_buses = set()
        
        queue = deque([(source, 0)])  # (current stop, buses taken)
        
        while queue:
            stop, buses = queue.popleft()
            
            for bus in stop_to_buses[stop]:
                if bus in used_buses:
                    continue
                
                used_buses.add(bus)
                
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1
                    
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))
        
        return -1