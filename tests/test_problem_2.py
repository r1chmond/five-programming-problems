from src import main

def test_combine_list_empty_lists():
    assert main.combine_list([],[]) == []

def test_combine_list_one_empty_list():
    assert main.combine_list([1,2,3], []) == [1,2,3]
    assert main.combine_list([], [1,2,3]) == [1,2,3]

def test_combine_list_asymmetric_lists():
    assert main.combine_list([7,6,9], [1]) == [7,1,6,9]
    assert main.combine_list([7], [-1,6,9]) == [7,-1,6,9]
    assert main.combine_list([7,6,9], [34,98]) == [7,34,6,98,9]
    assert main.combine_list([7,6], [34,98,9]) == [7,34,6,98,9]

def test_combine_list_symmetric_lists():
    assert main.combine_list([5,4,6], [2,5,-8]) == [5,2,4,5,6,-8]
    assert main.combine_list([-2,5,8], [-5,4,6]) == [-2,5,-5,4,8,6]

def test_combine_list_repeated_elements():
    assert main.combine_list([1,1,1], [1,1,1]) == [1,1,1,1,1,1]
    assert main.combine_list([1,1,1], [1,1]) == [1,1,1,1,1]
    assert main.combine_list([0,0,0], [0,0]) == [0,0,0,0,0]