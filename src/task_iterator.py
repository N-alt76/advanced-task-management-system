"""Custom iterator for traversing tasks in insertion order."""

from typing import Iterable, Iterator, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .task import Task


class TaskIterator(Iterator["Task"]):
    """Iterate over a snapshot of tasks without exposing the manager's list."""

    def __init__(self, tasks: Iterable["Task"]):
        self._tasks: List["Task"] = list(tasks)
        self._index = 0

    def __iter__(self) -> "TaskIterator":
        return self

    def __next__(self) -> "Task":
        if self._index >= len(self._tasks):
            raise StopIteration
        task = self._tasks[self._index]
        self._index += 1
        return task
