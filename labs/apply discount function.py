# remeber to use return instead of print in function body
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    elif not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    elif price <= 0:
        return 'The price should be greater than 0'
    elif discount > 100 or discount < 0:
        return 'The discount should be between 0 and 100'
    else:
        return price - (price*discount/100)


print(apply_discount(74.5, 90.0))
