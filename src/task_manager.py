"""Task collection and concurrent execution services."""

from threading import Lock, Thread
from typing import List

from .decorators import log_execution, measure_time
from .exceptions import InvalidTaskError, TaskNotFoundError
from .logger import get_logger
from .task import Task
from .task_iterator import TaskIterator


class TaskManager:
    """Store tasks, manage their lifecycle, and execute them concurrently."""

    def __init__(self):
        self._tasks: List[Task] = []
        self._lock = Lock()
        self._logger = get_logger()

    @log_execution
    def add_task(self, task: Task) -> None:
        """Add a valid task to the manager."""
        if not isinstance(task, Task):
            raise InvalidTaskError("Only Task objects can be added")
        with self._lock:
            if any(existing.task_id == task.task_id for existing in self._tasks):
                raise InvalidTaskError(f"Task ID {task.task_id} already exists")
            self._tasks.append(task)
        self._logger.info("Task added: %s", task)

    @log_execution
    def remove_task(self, task_id: int) -> Task:
        """Remove and return a task, or raise TaskNotFoundError."""
        with self._lock:
            for index, task in enumerate(self._tasks):
                if task.task_id == task_id:
                    removed_task = self._tasks.pop(index)
                    self._logger.info("Task removed: %s", removed_task)
                    return removed_task
        raise TaskNotFoundError(f"Task {task_id} was not found")

    def get_task(self, task_id: int) -> Task:
        """Return a task by ID, or raise TaskNotFoundError."""
        with self._lock:
            for task in self._tasks:
                if task.task_id == task_id:
                    return task
        raise TaskNotFoundError(f"Task {task_id} was not found")

    def display_tasks(self) -> None:
        """Print all tasks and their current status."""
        for task in self:
            print(task)

    @measure_time
    @log_execution
    def execute_all(self) -> None:
        """Run every current task on its own thread and wait for completion."""
        with self._lock:
            tasks = list(self._tasks)
        threads = [Thread(target=task.execute, name=f"task-{task.task_id}") for task in tasks]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def __iter__(self) -> TaskIterator:
        """Return the custom iterator for the manager's tasks."""
        with self._lock:
            return TaskIterator(self._tasks)
