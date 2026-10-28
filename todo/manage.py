def add_task(tasks, title):
    """Add a task with a unique id and return it."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Task title cannot be empty")
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": new_id, "title": title.strip(), "done": False}
    tasks.append(task)
    return task


def remove_task(tasks, task_id):
    """Remove the task with the given id."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    raise ValueError(f"Task {task_id} not found")
