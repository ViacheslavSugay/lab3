import pytest
from src.data_structures import Stack, Queue


def test_stack_push_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_peek():
    stack = Stack()
    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.peek() == 10


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True

    stack.push(5)
    assert stack.is_empty() == False

    stack.pop()
    assert stack.is_empty() == True


def test_stack_len():
    stack = Stack()
    assert len(stack) == 0

    stack.push(1)
    stack.push(2)
    assert len(stack) == 2

    stack.pop()
    assert len(stack) == 1


def test_stack_min():
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(8)
    stack.push(1)

    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 2


def test_stack_empty_errors():
    stack = Stack()
    with pytest.raises(IndexError, match="В стэке нет элементов!"):
        stack.pop()
    with pytest.raises(IndexError, match="В стэке нет элементов!"):
        stack.peek()
    with pytest.raises(IndexError, match="В стэке нет элементов!"):
        stack.min()


def test_queue_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_queue_front():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.front() == 10
    assert queue.dequeue() == 10
    assert queue.front() == 20


def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty() == True

    queue.enqueue(5)
    assert queue.is_empty() == False

    queue.dequeue()
    assert queue.is_empty() == True


def test_queue_len():
    queue = Queue()
    assert len(queue) == 0

    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2

    queue.dequeue()
    assert len(queue) == 1


def test_queue_empty_errors():
    queue = Queue()
    with pytest.raises(IndexError, match="В очереди нет элементов!"):
        queue.dequeue()
    with pytest.raises(IndexError, match="В очереди нет элементов!"):
        queue.front()