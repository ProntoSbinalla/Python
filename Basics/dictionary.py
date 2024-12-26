prices = {
    "box_of_spaghetti": 4,
    "lasagne": 5,
    "hamburger": 6,
}

quantity = {
    "box_of_spaghetti": 6,
    "lasagne": 10,
    "hamburger": 0,
}

money_spent = 0

for price in prices:
    money_spent += prices[price] * quantity[price]

print(f"Total money spent: ${money_spent}")