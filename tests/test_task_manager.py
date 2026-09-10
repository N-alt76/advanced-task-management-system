"""Unit tests for task management behavior."""

import unittest

from src.exceptions import InvalidTaskError, TaskNotFoundError
from src.task import SimpleTask, TaskStatus
from src.task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = TaskManager()

    def test_add_valid_task(self) -> None:
        task = SimpleTask(1, "Read chapter")
        self.manager.add_task(task)
        self.assertIs(self.manager.get_task(1), task)

    def test_reject_invalid_task(self) -> None:
        with self.assertRaises(InvalidTaskError):
            self.manager.add_task("not a task")  # type: ignore[arg-type]

    def test_remove_task(self) -> None:
        self.manager.add_task(SimpleTask(1, "Temporary"))
        removed = self.manager.remove_task(1)
        self.assertEqual(removed.name, "Temporary")
        with self.assertRaises(TaskNotFoundError):
            self.manager.get_task(1)

    def test_remove_missing_task(self) -> None:
        with self.assertRaises(TaskNotFoundError):
            self.manager.remove_task(99)

    def test_execute_all_completes_tasks(self) -> None:
        first = SimpleTask(1, "First", duration=0.01)
        second = SimpleTask(2, "Second", duration=0.01)
        self.manager.add_task(first)
        self.manager.add_task(second)
        self.manager.execute_all()
        self.assertEqual(first.status, TaskStatus.COMPLETED)
        self.assertEqual(second.status, TaskStatus.COMPLETED)


if __name__ == "__main__":
    unittest.main()
