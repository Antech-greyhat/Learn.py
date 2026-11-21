# Process urgent tasks first, preserving arrival order for equal priorities.
# Practice: dataclasses, heaps, ordering, classes, and exceptions.
from dataclasses import dataclass, field
import heapq
from itertools import count


@dataclass(order=True)
class Task:
    priority: int
    task_id: int
    name: str = field(compare=False)


class TaskQueue:
    def __init__(self):
        self.tasks = []
        self.next_id = count(1)

    def add(self, name, priority):
        name = name.strip()
        if not name:
            raise ValueError("Task name cannot be empty.")
        if type(priority) is not int or not 1 <= priority <= 5:
            raise ValueError("Priority must be a whole number from 1 to 5.")
        task = Task(priority, next(self.next_id), name)
        heapq.heappush(self.tasks, task)
        return task.task_id

    def next_task(self):
        if not self.tasks:
            raise ValueError("No tasks waiting.")
        return heapq.heappop(self.tasks)

    def cancel(self, task_id):
        for index, task in enumerate(self.tasks):
            if task.task_id == task_id:
                removed = self.tasks.pop(index)
                # Removing an arbitrary entry requires restoring heap order.
                heapq.heapify(self.tasks)
                return removed
        raise ValueError("Task ID not found.")

    def pending(self):
        # A heap's internal list is only partially ordered.
        return sorted(self.tasks)


def main():
    queue = TaskQueue()
    print("Priority Task Queue - 1 is most urgent; tasks last for this session.")
    while True:
        print("\n1. Add task\n2. Process next\n3. View pending\n4. Cancel task\n5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                name = input("Task name: ")
                priority = int(input("Priority (1-5): "))
                print(f"Added task #{queue.add(name, priority)}.")
            elif choice == "2":
                task = queue.next_task()
                print(f"Processed #{task.task_id}: {task.name}")
            elif choice == "3":
                tasks = queue.pending()
                if not tasks:
                    print("No tasks waiting.")
                for task in tasks:
                    print(f"#{task.task_id} | Priority {task.priority} | {task.name}")
            elif choice == "4":
                task = queue.cancel(int(input("Task ID: ")))
                print(f"Cancelled #{task.task_id}: {task.name}")
            elif choice == "5":
                break
            else:
                print("Choose an option from 1 to 5.")
        except ValueError as error:
            print(f"Queue unchanged: {error}")


if __name__ == "__main__":
    main()
