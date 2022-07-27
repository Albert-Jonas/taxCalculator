from CalculateTax import calculate_tax


def test_calculate_tax_first_third():
    assert calculate_tax(7500) == 0
    assert calculate_tax(10000) == 0


#def test_calculate_tax_second_third():
#    assert calculate_tax(15000) == 500
#    assert calculate_tax(20000) == 1000


#def test_calculate_tax_third_third():
#    assert calculate_tax(25000) == 2000
#    assert calculate_tax(45000) == 6000
