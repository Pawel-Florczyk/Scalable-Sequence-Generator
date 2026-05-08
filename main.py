from typing import Generator


class SequenceGenerator:
    def __init__(self, name: str, num0: int, num1: int) -> None:
        if not isinstance(num0, int) or not isinstance(num1, int):
            raise ValueError

        self.name = name
        self.num0 = num0
        self.num1 = num1

    def sequence(self, long_of_sequence: int) -> Generator[int, None, None]:
        f0, f1 = self.num0, self.num1
        for i in range(long_of_sequence):
            yield f0
            f0, f1 = f1, f0 + f1

    def is_in_sequence(self, target: int) -> bool:
        f0, f1 = self.num0, self.num1
        while f0 <= target:
            if f0 == target:
                return True
            f0, f1 = f1, f0 + f1
        return False

    def __enter__(self):
        self.file = open(f"{self.name}.txt", "w", encoding="utf-8")
        print("steam is open")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("steam is closed")
        self.file.close()
