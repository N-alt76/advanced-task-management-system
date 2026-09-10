"""Custom exceptions used by the task management system."""


class TaskError(Exception):
    """Base exception for task-related errors."""


class InvalidTaskError(TaskError):
    """Raised when a task is missing or has invalid data."""


class TaskNotFoundError(TaskError):
    """Raised when a requested task does not exist."""
