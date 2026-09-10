# AMS Project Explanation

## 1. Problem Statement

Small task collections are easy to manage manually, but they are useful practice for organizing objects, tracking state, and coordinating independent work. AMS models that problem with a small command-line task manager.

## 2. Project Objective

The objective is to demonstrate core Python concepts through a readable task management application. The project focuses on object-oriented design, custom iteration, decorators, multithreading, logging, exceptions, and testing without external dependencies.

## 3. Architecture

The `src` package contains the application code. `Task` is the abstract domain object, while `SimpleTask` and `PriorityTask` provide concrete behavior. `TaskManager` owns a collection of tasks and coordinates their execution. `TaskIterator` exposes safe insertion-order traversal. Supporting modules provide decorators, logging, and exceptions. The `tests` package exercises the public manager behavior.

The manager protects its task collection with a lock. During execution it takes a snapshot, starts one thread per task, and joins every thread before returning.

## 4. OOP Concepts Used

- **Abstraction:** `Task` is an abstract base class with an abstract `execute()` method.
- **Inheritance:** `SimpleTask` and `PriorityTask` inherit shared validation and status behavior from `Task`.
- **Polymorphism:** The manager can execute any `Task` object without checking its concrete class. Each class supplies its own `execute()` implementation.
- **Encapsulation:** Task state and the manager's collection are controlled through methods, with locks protecting mutable state during concurrent work.

## 5. Iterator Implementation

`TaskIterator` implements Python's iterator protocol with `__iter__()` and `__next__()`. It works on a snapshot of the manager's tasks, so callers can use normal `for` loops without accessing the manager's internal list directly.

## 6. Decorator Implementation

`log_execution` records when a decorated function starts, finishes, or raises an exception. `measure_time` uses `time.perf_counter()` to record elapsed time. `functools.wraps` preserves the wrapped function's name and documentation. `TaskManager` uses these decorators on task operations that are useful to observe.

## 7. Multithreading Implementation

`TaskManager.execute_all()` creates a `threading.Thread` for each task, starts all threads, and calls `join()` for each one. This lets independent simulated tasks run concurrently while still ensuring the manager does not return early. Since scheduling is controlled by the operating system, output order is not fixed.

## 8. Exception Handling Strategy

The manager raises `InvalidTaskError` for invalid objects and duplicate IDs, and `TaskNotFoundError` for unknown IDs. Task execution catches unexpected execution errors, changes the task state to `FAILED`, stores a readable error message, logs the failure, and re-raises the exception so the caller can decide how to handle it.

## 9. Challenges Faced

- Managing thread completion correctly using `join()`.
- Handling unpredictable execution order in multithreading.
- Designing reusable decorators that preserve function metadata.
- Designing custom exceptions with clear responsibilities.
- Maintaining task status correctly while a task changes state on a worker thread.

## 10. Learning Outcomes

This project provides practice designing a small package, separating responsibilities across modules, using abstract classes and inheritance, writing a custom iterator, applying decorators, coordinating threads, protecting shared state with locks, recording useful logs, handling domain errors, and writing focused unit tests.
