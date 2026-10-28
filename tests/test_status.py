import pytest
from todo.status import complete_task, filter_by_status, completion_percentage


def make_tasks():
    return [
        {"title": "Buy milk", "done": True},
        {"title": "Study", "done": False},
        {"title": "Gym", "done": False},
        {"title": "Read", "done": False},
    ]


def test_complete_task_marks_done():                 # normal behavior
    tasks = make_tasks()
    complete_task(tasks, "Study")
    assert tasks[1]["done"] is True


def test_filter_pending_tasks():                     # normal behavior
    result = filter_by_status(make_tasks(), False)
    assert [t["title"] for t in result] == ["Study", "Gym", "Read"]


def test_completion_percentage():                    # normal behavior
    assert completion_percentage(make_tasks()) == 25.0


def test_completion_percentage_empty_list():         # edge case
    assert completion_percentage([]) == 0.0