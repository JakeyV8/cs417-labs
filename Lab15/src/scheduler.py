"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    """A priority-based task scheduler.

    Tasks are added with a priority (lower number = more urgent).
    Tasks with the same priority are processed in FIFO order.
    """

    def __init__(self):
        """Initialize the scheduler."""
        # TODO: Set up your internal data structures
        self.schedule = []

    def add_task(self, priority, description):
        """Add a task to the scheduler.

        Args:
            priority: An integer priority (lower = more urgent).
            description: A string describing the task.
        """
        # TODO: Push onto the heap with a tiebreaker
        heapq.heappush(self.schedule,(priority,description))

    def next_task(self):
        """Remove and return the highest-priority task's description.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Pop from the heap, return the description
        if len(self.schedule) == 0:
            return None
        smallest = heapq.heappop(self.schedule)
        return smallest[-1]

    def peek(self):
        """Return the highest-priority task's description without removing it.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Look at h[0] without popping
        if len(self.schedule) == 0:
            return None
        return self.schedule[0][-1]

    def __len__(self):
        """Return the number of pending tasks."""
        # TODO: Return the length of the heap
        return len(self.schedule)

    def is_empty(self):
        """Return True if there are no pending tasks."""
        # TODO
        if len(self.schedule) == 0:
            return True
        else:
            return False