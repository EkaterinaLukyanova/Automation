def bank(x, y):
    total = x # начальная сумма вклада
    for i in range(y):
        total += total * 0.10 # увеличиваем сумму вклада на 10% каждый год
    return total
print(bank(1000, 5))