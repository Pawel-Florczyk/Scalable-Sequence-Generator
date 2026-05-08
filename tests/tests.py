from main import SequenceGenerator
import pytest
import os


class TestSequenceLogic:

    def test_incorrect_type_of_data(self):
        with pytest.raises(ValueError):
            SequenceGenerator("manager", 0, "s")

class TestSequenceIO:

    def test_read_file_of_sequence(self):
        fibonacci = SequenceGenerator("fibonacci", 0, 1)
        with fibonacci as f:
            for num in f.sequence(100):
                f.file.write(f"{num}\n")
        with open("fibonacci.txt", "r") as s:
            lines = s.readlines()
            assert len(lines) == 100
            assert lines[0].strip() == "0"


@pytest.mark.parametrize("index,expected_value",
                         [
                             (0, 0),
                             (1, 1),
                             (4, 3),
                             (9, 34)
                         ])
def test_fibonacci_values(index: int, expected_value: int):
    manager = SequenceGenerator("manager", 0, 1)
    results = list(manager.sequence(index + 1))
    assert results[index] == expected_value

@pytest.fixture
def sequence_manager():
    m = SequenceGenerator("manager", 0, 1)
    yield m

    if os.path.exists("manager"):
        os.remove("manager")

def test_example(sequence_manager: SequenceGenerator):
    assert sequence_manager.is_in_sequence(5) == True
