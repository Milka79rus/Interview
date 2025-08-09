"""
stack_checker.py

Реализация класса Stack и функция is_balanced для проверки
сбалансированности скобок. Вывод в консоль:
'Сбалансированно' или 'Несбалансированно'.
"""


from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    """Простой стек на базе списка."""

    def __init__(self) -> None:
        self._items: List[T] = []


    def is_empty(self) -> bool:
        """Возвращает True, если стек пуст."""    
        return len(self._items) == 0
    
    def push(self, item: T) -> None:
        """Добавляет элемент на вершину стека."""
        self._items.append(item)


    def pop(self) -> T:
        """Удаляет и возвращает верхний элемент стека.
        
        Raises:
            IndexError: если стек пуст.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    

    def peek(self) -> Optional[T]:
        """Возвращает верхний элемент стека, но не удаляет его.
        Если стек пуст, возвращает None.
        """
        if self.is_empty():
            return None
        return self._items[-1]
    

    def size(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self._items)
    

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"
    

def is_balanced(s: str) -> bool:
    """
    Проверяет, сбалансирована ли строка скобок.
    Игнорирует пррчие символы - обрабатываются только (), [], {}.
    """   
    pairs = {")": "(", "]": "[", "}": "{"}
    openings = set(pairs.values())
    stack = Stack[str]()

    for ch in s:
        if ch in openings:
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False
            
    return stack.is_empty()        


def _demo_examples() -> None:
    """Пара примеров."""
    examples = [
        "(((({{}}))))",
        "([()])",
        "{{[()]}}",
        "}{",
        "{{[(])}}",
        "[[[(]]",
        "",  # пустая строка — сбалансирована
        "a+(b*c)-{d/e}"  # игнорируем не-скобочные символы        
    ]
    for s in examples:
        result = "Сбалансированно" if is_balanced(s) else "Несбалансированно"
        print(f"{s!r}: {result}")


if __name__ == "__main__":
    # Если вызывают напрямую — короткая демонстрация и интерактивный ввод.
    _demo_examples()
    try:
        text = input("\nВведите строку со скобками (или Enter чтобы выйти): ").strip()
        if text:
            print("Сбалансированно" if is_balanced(text) else "Несбалансированно")
    except (KeyboardInterrupt, EOFError):
        print("\nВыход.")