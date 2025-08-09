import pytest
from stack_checker import is_balanced


@pytest.mark.parametrize("expr", [
    "(((({{}}))))",
    "([()])",
    "{{[()]}}",
    "",  # пустая строка — сбалансирована
    "a+(b*c)-{d/e}",  # с посторонними символами
])
def test_balanced(expr):
    assert is_balanced(expr)


@pytest.mark.parametrize("expr", [
    "}{",
    "{{[(])}}",
    "[[[(]]",
    "(",
    "())",
])
def test_unbalanced(expr):
    assert not is_balanced(expr)
