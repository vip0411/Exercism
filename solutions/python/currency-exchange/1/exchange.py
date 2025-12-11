def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    return int(amount // denomination)

def get_leftover_of_bills(amount, denomination):
    whole_bills = get_number_of_bills(amount, denomination)
    return amount - (whole_bills * denomination)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    effective_rate = exchange_rate * (1 + (spread / 100.0))
    foreign_amount = budget / effective_rate
    whole_bills = int(foreign_amount // denomination)
    return whole_bills * denomination