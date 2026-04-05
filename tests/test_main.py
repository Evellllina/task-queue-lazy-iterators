import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.task import Task, TaskStatus
from src.task_queue import TaskQueue


def test_task_creation1():
    task = Task(id=1, priority=2, status=TaskStatus.PENDING, payload="test")
    assert task.id == 1


def test_task_creation2():
    task = Task(id=1, priority=2, status=TaskStatus.PENDING, payload="test")
    assert task.priority == 2


def test_task_creation3():
    task = Task(id=1, priority=2, status=TaskStatus.PENDING, payload="test")
    assert task.status == TaskStatus.PENDING


def test_task_creation4():
    task = Task(id=1, priority=2, status=TaskStatus.PENDING, payload="test")
    assert task.payload == "test"


def test_empty_queue():
    queue = TaskQueue()
    assert len(queue) == 0


def test_queue_with_none():
    queue = TaskQueue(None)
    assert len(queue) == 0


def test_queue_with_tasks():
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "a"),
        Task(2, 2, TaskStatus.COMPLETED, "b"),
    ]
    queue = TaskQueue(tasks)
    assert len(queue) == 2


def test_add_one_task():
    queue = TaskQueue()
    task = Task(1, 1, TaskStatus.PENDING, "data")
    queue.add(task)
    assert len(queue) == 1


def test_add_all_tasks():
    queue = TaskQueue()
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "a"),
        Task(2, 2, TaskStatus.COMPLETED, "b"),
    ]
    queue.add_all(tasks)
    assert len(queue) == 2


def test_iteration():
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "a"),
        Task(2, 2, TaskStatus.COMPLETED, "b"),
    ]
    queue = TaskQueue(tasks)
    result = [task.id for task in queue]
    assert result == [1, 2]


def test_filter_by_status_pending():
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "a"),
        Task(2, 2, TaskStatus.COMPLETED, "b"),
        Task(3, 3, TaskStatus.PENDING, "c"),
    ]
    queue = TaskQueue(tasks)
    result = [task.id for task in queue.filter_by_status(TaskStatus.PENDING)]
    assert result == [1, 3]


def test_len():
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "a"),
        Task(2, 2, TaskStatus.PENDING, "b"),
    ]
    queue = TaskQueue(tasks)
    assert len(queue) == 2


def test_getitem():
    tasks = [
        Task(1, 1, TaskStatus.PENDING, "a"),
        Task(2, 2, TaskStatus.PENDING, "b"),
    ]
    queue = TaskQueue(tasks)
    assert queue[0].id == 1
    assert queue[1].id == 2