from src import main

def test_sum_of_an_empty_list():
    assert main.list_sum_for_loop([]) == 0
    assert main.list_sum_while_loop([]) == 0
    assert main.list_sum_recursion([]) == 0

def test_sum_of_list_with_one_element():
    assert main.list_sum_for_loop([1]) == 1
    assert main.list_sum_while_loop([1]) == 1
    assert main.list_sum_recursion([1]) == 1

def test_sum_of_list_with_repeated_elements():
    assert main.list_sum_for_loop([1,1,1,1,1,1,1,1,1,1]) == 10
    assert main.list_sum_while_loop([1,1,1,1,1,1,1,1,1,1]) == 10
    assert main.list_sum_recursion([1,1,1,1,1,1,1,1,1,1]) == 10

def test_sum_of_list_with_large_num_of_element():
    assert main.list_sum_for_loop([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]) == 180
    assert main.list_sum_while_loop([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]) == 180
    assert main.list_sum_recursion([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]) == 180

