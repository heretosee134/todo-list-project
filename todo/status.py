def complete_task(tasks, title):
    for task in tasks:
        if task["title"] == title:
            if task["done"]:
                raise ValueError(f"Task already completed: {title}")
            task["done"] = True
            return task
    raise ValueError(f"Task not found: {title}")


def filter_by_status(tasks, done):
    if not isinstance(done, bool):
        raise ValueError("done must be True or False")
    return [task for task in tasks if task["done"] == done]


def completion_percentage(tasks):
    if not tasks:
        return 0.0
    done_count = len(filter_by_status(tasks, True))
    return round(done_count / len(tasks) * 100, 1)