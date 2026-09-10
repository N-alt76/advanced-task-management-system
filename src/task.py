"""Task abstractions and concrete task implementations."""

from abc import ABC, abstractmethod
from enum import Enum
import time
from threading import Lock

from .logger import get_logger


class TaskStatus(Enum):
    """Possible states in a task's lifecycle."""

    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Task(ABC):
    """Abstract base class shared by all task types."""

    def __init__(self, task_id: int, name: str, duration: float = 0.1):
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("task_id must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if duration < 0:
            raise ValueError("duration cannot be negative")
        self.task_id = task_id
        self.name = name.strip()
        self.duration = duration
        self.status = TaskStatus.PENDING
        self.error: str | None = None
        self._status_lock = Lock()

    def _start(self) -> None:
        with self._status_lock:
            self.status = TaskStatus.RUNNING
            self.error = None
        get_logger().info("Task created/executing: %s", self)

    def _complete(self) -> None:
        with self._status_lock:
            self.status = TaskStatus.COMPLETED
        get_logger().info("Task completed: %s", self)

    def _fail(self, error: Exception) -> None:
        with self._status_lock:
            self.status = TaskStatus.FAILED
            self.error = str(error)
        get_logger().exception("Task failed: %s", self)

    @abstractmethod
    def execute(self) -> str:
        """Execute the task and return a short result message."""

    def __str__(self) -> str:
        return f"#{self.task_id} {self.name} [{self.status.value}]"


class SimpleTask(Task):
    """A regular task that completes after a simulated duration."""

    def execute(self) -> str:
        self._start()
        try:
            time.sleep(self.duration)
            self._complete()
            return f"Simple task '{self.name}' completed"
        except Exception as error:
            self._fail(error)
            raise


class PriorityTask(Task):
    """A task with a priority value, demonstrating a specialized implementation."""

    def __init__(self, task_id: int, name: str, priority: int, duration: float = 0.1):
        super().__init__(task_id, name, duration)
        if priority < 1:
            raise ValueError("priority must be at least 1")
        self.priority = priority

    def execute(self) -> str:
        self._start()
        try:
            time.sleep(self.duration)
            self._complete()
            return f"Priority task '{self.name}' completed (priority {self.priority})"
        except Exception as error:
            self._fail(error)
            raise
