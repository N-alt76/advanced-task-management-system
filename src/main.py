"""Command-line demonstration for AMS."""

from .task import PriorityTask, SimpleTask
from .task_manager import TaskManager


def main() -> None:
    """Create sample tasks, display them, and execute them concurrently."""
    manager = TaskManager()
    manager.add_task(SimpleTask(1, "Prepare report", duration=0.2))
    manager.add_task(PriorityTask(2, "Back up files", priority=1, duration=0.1))
    manager.add_task(SimpleTask(3, "Send summary", duration=0.15))

    print("Tasks before execution:")
    manager.display_tasks()
    print("\nExecuting tasks concurrently...")
    manager.execute_all()
    print("\nTasks after execution:")
    manager.display_tasks()


if __name__ == "__main__":
    main()
