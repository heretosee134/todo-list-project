def complete_task(tasks, title):
    for task in tasks:
        if task["title"] == title:
            task["done"] = True
            return task


def filter_by_status(tasks, done):
    return [task for task in tasks if task["done"] == done]


def completion_percentage(tasks):
    if not tasks:
        return 0.0
    done_count = len(filter_by_status(tasks, True))
    return round(done_count / len(tasks), 1)