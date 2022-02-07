numbers = [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8, 1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]

def sum_odds(_numbers) -> int:

    sum = 0
    for i in _numbers:
        if i % 2 != 0:
            sum += i
    return sum


sum_lambda_odds = lambda a: sum_odds(a)

print(sum_lambda_odds(numbers))