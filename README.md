# AMS - Advanced Multi-threaded Task Management System

## Overview

AMS is a Python learning project that demonstrates important Python programming concepts through a practical task management application. It supports different task types, tracks task status, and executes independent tasks concurrently with Python threads.

## Features

- Add simple and priority-based tasks.
- Display task names, IDs, and statuses.
- Execute tasks concurrently with `threading.Thread`.
- Track `Pending`, `Running`, `Completed`, and `Failed` states.
- Iterate through tasks with a custom iterator.
- Log function execution and measure execution time with decorators.
- Write application activity to `ams.log` and the console.
- Raise custom exceptions for invalid and missing tasks.
- Run unit tests with Python's built-in `unittest` framework.

## Concepts Demonstrated

| Concept | Implementation in Project |
| --- | --- |
| OOP | Task classes and `TaskManager` |
| Abstraction | Abstract `Task` base class |
| Inheritance | `SimpleTask` and `PriorityTask` |
| Polymorphism | Different `execute()` implementations |
| Iterator | Custom `TaskIterator` |
| Decorators | Logging and execution timing |
| Multithreading | Concurrent task execution with `threading.Thread` |
| Exception Handling | `InvalidTaskError` and `TaskNotFoundError` |
| Logging | Python `logging` module with file and console handlers |
| Testing | Built-in `unittest` |

## Project Architecture

- `src/task.py`: Defines `Task`, `SimpleTask`, `PriorityTask`, and task statuses.
- `src/task_manager.py`: Adds, removes, displays, and concurrently executes tasks.
- `src/task_iterator.py`: Provides insertion-order iteration over a task snapshot.
- `src/decorators.py`: Contains decorators for logging and timing function calls.
- `src/exceptions.py`: Defines task-related custom exceptions.
- `src/logger.py`: Configures the shared file and console logger.
- `src/main.py`: Runs the command-line demonstration.
- `tests/test_task_manager.py`: Covers the main manager and execution behaviors.
- `docs/project_explanation.md`: Explains the design and learning goals.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/advanced-task-management-system.git
   ```

2. Navigate into the project directory:

   ```bash
   cd advanced-task-management-system
   ```

3. Use Python 3.10 or newer. AMS uses only the standard library, so no package installation is required. An optional virtual environment can be created with:

   ```bash
   python -m venv .venv
   ```

## Usage

Run the demonstration from the repository root:

```bash
python -m src.main
```

Example output (threaded log lines may appear in a different order):

```text
Tasks before execution:
#1 Prepare report [Pending]
#2 Back up files [Pending]
#3 Send summary [Pending]

Executing tasks concurrently...

Tasks after execution:
#1 Prepare report [Completed]
#2 Back up files [Completed]
#3 Send summary [Completed]
```

The application also creates `ams.log` in the working directory. The log contains task events, exceptions, thread names, and decorator timing information.

## How Multithreading Works

`TaskManager.execute_all()` takes a snapshot of the current tasks, creates one `threading.Thread` for each task, starts every thread, and then calls `join()` on each thread. `join()` ensures the method waits until all tasks finish. Because the threads run independently, completion and log order may vary between runs.

## Error Handling

`InvalidTaskError` is raised when a non-`Task` object is added or a duplicate task ID is used. `TaskNotFoundError` is raised when code tries to remove or retrieve an ID that is not present. Individual task implementations mark themselves as `Failed` and record the error if execution raises an exception.

## Testing

Run all unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests cover adding a valid task, rejecting an invalid task, removing a task, handling a missing task, and verifying completed execution status.

## Future Improvements

The following are possible future improvements and are not currently implemented:

- SQLite persistence.
- A REST API.
- Task scheduling.
- User authentication.
- A web interface.

## Learning Outcomes

Building AMS provides practice with abstract base classes, inheritance, polymorphism, encapsulation of mutable state, custom iterators, decorators, threads, locks, logging, custom exceptions, file output, and unit testing.

## Author

Your Name - [GitHub Profile](https://github.com/your-username)
