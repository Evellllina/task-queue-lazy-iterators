from typing import Optional, List, Iterator, Callable
from task import Task, TaskStatus
from task_queue_iterator import TaskQueueIterator

class TaskQueue:
    """Очередь задач с поддержкой итерации и фильтрации"""
    def __init__(self, tasks: Optional[List[Task]] = None):
        self._tasks = tasks if tasks is not None else []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def add_all(self, tasks: List[Task]) -> None:
        self._tasks.extend(tasks)

    def __len__(self) -> int:
        return len(self._tasks)

    def __getitem__(self, index: int) -> Task:
        return self._tasks[index]

    def __iter__(self) -> Iterator[Task]:
        return TaskQueueIterator(self._tasks)

    def filter_by_status(self, status: TaskStatus) -> Iterator[Task]: #Возвращает задачи с определённым статусом
        for task in self._tasks:
            if task.status == status:
                yield task

    def filter_by_priority(self, max_priority: int) -> Iterator[Task]: #Фильтрует по приоритету
        for task in self._tasks:
            if task.priority <= max_priority:
                yield task

    def filter(self, predicate: Callable[[Task], bool]) -> Iterator[Task]: #Принимает функцию-предикат, которая решает, подходит задача или нет.
        for task in self._tasks:
            if predicate(task):
                yield task

    def get_pending_tasks(self) -> Iterator[Task]:#берёт все задачи, у которых статус PENDING
        return self.filter_by_status(TaskStatus.PENDING)

    def get_high_priority_pending(self) -> Iterator[Task]: #берёт все задачи, у которых статус PENDING и приоритет меньше 3
        return (task for task in self._tasks
                if task.status == TaskStatus.PENDING and task.priority <= 2)