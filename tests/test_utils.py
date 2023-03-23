import pytest
from utils.utils import correct_input, change_calculation


def test_sum_total_not_alpha():
    with pytest.raises(TypeError):
        correct_input('любая буква может быть здесь', '12000')

def test_deposited_pennies_bigger_than_99():
    with pytest.raises(ValueError):
        correct_input('10000', '13000.192')

def test_enough_money():
    with pytest.raises(ValueError):
        correct_input('12000', '5000 5000')

def test_existing_banknotes():
    with pytest.raises(ValueError):
        correct_input('9999', '3000 3000 5000')



@pytest.mark.parametrize('all_total, all_money, result', [(12000, 15000, '1000 1000 1000'),
                                                          (10000, 15000, '5000'),
                                                          (5000, 5000, ''),
                                                          (9850, 10000, '100 50' ),
                                                          (1250, 5000, '1000 1000 1000 500 100 100 50')])
def test_correct_change(all_total, all_money, result):
    assert change_calculation(all_total, all_money) == result