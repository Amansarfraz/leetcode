import 'dart:math';
import 'package:collection/collection.dart';

class Server {
  final int index;
  final int weight;
  int freeTime;

  Server(this.index, this.weight, [this.freeTime = 0]);
}

class Solution {
  List<int> assignTasks(List<int> servers, List<int> tasks) {
    // Min-heap for idle servers: prioritize by weight, then by index
    final idleServers = PriorityQueue<Server>((a, b) {
      if (a.weight != b.weight) {
        return a.weight.compareTo(b.weight);
      }
      return a.index.compareTo(b.index);
    });

    // Min-heap for busy servers: prioritize by freeTime, then weight, then index
    final busyServers = PriorityQueue<Server>((a, b) {
      if (a.freeTime != b.freeTime) {
        return a.freeTime.compareTo(b.freeTime);
      }
      if (a.weight != b.weight) {
        return a.weight.compareTo(b.weight);
      }
      return a.index.compareTo(b.index);
    });

    // Initialize all servers into the idle queue
    for (int i = 0; i < servers.length; i++) {
      idleServers.add(Server(i, servers[i]));
    }

    final List<int> result = List<int>.filled(tasks.length, 0);
    int currentTime = 0;

    for (int i = 0; i < tasks.length; i++) {
      // The current task becomes available at least at time `i`
      currentTime = max(currentTime, i);

      // Fast-forward time if no idle servers are available
      if (idleServers.isEmpty && busyServers.isNotEmpty) {
        currentTime = max(currentTime, busyServers.first.freeTime);
      }

      // Move all servers that have finished processing by currentTime to the idle queue
      while (busyServers.isNotEmpty && busyServers.first.freeTime <= currentTime) {
        idleServers.add(busyServers.removeFirst());
      }

      // Assign the task to the best available idle server
      final currentServer = idleServers.removeFirst();
      result[i] = currentServer.index;
      
      // Calculate next available time and push to the busy queue
      currentServer.freeTime = currentTime + tasks[i];
      busyServers.add(currentServer);
    }

    return result;
  }
}
