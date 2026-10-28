import pytest
from todo.manage import add_task, remove_task


def test_add_task_normal():
    tasks = []
    task = add_task(tasks, "Buy milk")
    assert task["title"] == "Buy milk"
    assert task["done"] is False
    assert len(tasks) == 1


def test_add_task_strips_spaces_edge_case():
    tasks = []
    assert add_task(tasks, "   Study   ")["title"] == "Study"


def test_add_task_empty_title_raises():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_remove_task_normal():
    tasks = []
    add_task(tasks, "A")
    assert remove_task(tasks, 1) is True
    assert tasks == []


def test_remove_missing_task_raises():
    with pytest.raises(ValueError):
        remove_task([], 99)
