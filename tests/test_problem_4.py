from src import main

def test_largest_formed_number_with_empty_list():
    assert main.largest_formed_number([]) == 0 

def test_largest_formed_number_with_one_element():
    assert main.largest_formed_number([19]) == 19
    assert main.largest_formed_number([1]) == 1
    assert main.largest_formed_number([23]) == 23

def test_largest_formed_number_with_repeated_elements():
    assert main.largest_formed_number([1,1,1,1,1]) == 11_111
    assert main.largest_formed_number([8,8,8,8,8]) == 88_888

def test_largest_formed_number():
    assert main.largest_formed_number([50,2,1,9]) == 95021
    assert main.largest_formed_number([20,5,18,9]) == 952018


