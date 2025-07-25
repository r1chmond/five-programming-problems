from src import main

def test_all_possible_expressions():
    expected_solution = [
        "1 + 2 + 3 - 4 + 5 + 6 + 78 + 9",
                "1 + 2 + 34 - 5 + 67 - 8 + 9",
                "1 + 23 - 4 + 5 + 6 + 78 - 9",
                "1 + 23 - 4 + 56 + 7 + 8 + 9",
                "12 + 3 + 4 + 5 - 6 - 7 + 89",
                "12 + 3 - 4 + 5 + 67 + 8 + 9",
                "12 - 3 - 4 + 5 - 6 + 7 + 89",
                "123 + 4 - 5 + 67 - 89",
                "123 + 45 - 67 + 8 - 9",
                "123 - 4 - 5 - 6 - 7 + 8 - 9",
                "123 - 45 - 67 + 89"
    ]
    assert main.all_possible_expressions() == expected_solution