import pytest
from stack_checker import Stack


def test_stack_initially_empty():
    stack = Stack()
    assert stack.is_empty()
    assert stack.size() == 0
    assert stack.peek() is None


def test_push_increases_size():
    stack = Stack()
    stack.push(1)
    assert not stack.is_empty()
    assert stack.size() == 1
    assert stack.peek() == 1


def test_pop_returns_last_item():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    item = stack.pop()
    assert item == "b"
    assert stack.size() == 1
    assert stack.peek() == "a"


def test_pop_from_empty_stack_raises():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_does_not_remove_item():
    stack = Stack()
    stack.push(42)
    top = stack.peek()
    assert top == 42
    assert stack.size() == 1
