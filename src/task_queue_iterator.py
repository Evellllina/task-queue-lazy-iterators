from typing import List, Iterator
from task import Task

class TaskQueueIterator:
    """Итератор для обхода очереди задач"""
    def __init__(self, tasks: List[Task]):
        """Инициализирует итератор списком задач"""
        self._tasks = tasks
        self._index = 0

    def __iter__(self) -> Iterator[Task]:
        return self

    def __next__(self) -> Task:
        """Возвращает следующую задачу при обходе"""
        if self._index >= len(self._tasks):
            raise StopIteration
        task = self._tasks[self._index]
        self._index += 1
        return task