from task import Task, TaskStatus
from task_queue import TaskQueue

if __name__ == "__main__":
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "process order"),
        Task(2, 3, TaskStatus.COMPLETED, "send email"),
        Task(3, 2, TaskStatus.PENDING, "update cache"),
        Task(4, 1, TaskStatus.RUNNING, "generate report"),
        Task(5, 4, TaskStatus.PENDING, "backup data"),
        Task(6, 2, TaskStatus.FAILED, "sync external"),
    ]

    queue = TaskQueue(tasks)

    print("Итерация")
    for task in queue:
        print(f"  {task.id}: {task.status.value}")

    print("\nПовторный обход")
    print([t.id for t in queue])
    print([t.id for t in queue])

    print("\nФильтр по статусу PENDING")
    for task in queue.filter_by_status(TaskStatus.PENDING):
        print(f"  {task.id}")

    print("\nФильтр по приоритету <= 2")
    for task in queue.filter_by_priority(2):
        print(f"  {task.id}")

    print("\nВысокий приоритет и PENDING")
    for task in queue.get_high_priority_pending():
        print(f"  {task.id}")

    print("\nУниверсальный фильтр")
    for task in queue.filter(lambda t: t.status in (TaskStatus.COMPLETED, TaskStatus.FAILED)):
        print(f"  {task.id}")

    print(f"\nКоличество PENDING: {sum(1 for _ in queue.filter_by_status(TaskStatus.PENDING))}")