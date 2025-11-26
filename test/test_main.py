from main.main import knapsack


def test_empty_case_all_empty():
    weights = []
    values = []
    max_weight = 0
    
    # act
    result = knapsack(weights, values, max_weight)
    # assert
    assert result == 0


def test_normal_case_target_can_find_1():
    weights = [10,20,30]
    values = [60,100,120]
    max_weight = 50
    
    # act
    result = knapsack(weights, values, max_weight)
    # assert
    assert result == 220


def test_normal_case_target_can_find_2():
    weights = [99, 60, 70, 68, 50, 65, 48, 31, 52, 29]
    values = [104, 105, 138, 135, 82, 73, 103, 52, 57, 136]
    max_weight = 75
    
    # act
    result = knapsack(weights, values, max_weight)
    # assert
    assert result == 188
