from enum import Enum
from dataclasses import dataclass
from typing import Any

class TaskStatus(Enum):
    """Статусы жизненного цикла задачи"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    """Модель задачи платформы обработки"""
    id: int
    priority: int
    status: TaskStatus
    payload: Any
    created_at: float = None

    def __post_init__(self):
        if self.created_at is None:
            import time
            self.created_at = time.time()