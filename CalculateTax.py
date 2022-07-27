def calculate_tax(users_income):
    tax_to_pay = 0
    if users_income / 10000 < 1:
        tax_to_pay += users_income * 0
    elif users_income / 10000 < 2:
        tax_to_pay += (users_income - 10000) * 0.1
    else:
        tax_to_pay = 10000 * 0.1
        tax_to_pay += (users_income - 20000) * 0.2
    return tax_to_pay
