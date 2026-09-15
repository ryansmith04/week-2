import numpy as np


# update/add code below ...

def ways(n):
    count = 0

    for nickels in range(n // 5 + 1):
        pennies = n - (nickels * 5)

        if pennies >= 0:
            count += 1

    return count

def lowest_score(names, scores):
    index = np.argmin(scores)
    return names[index]

def sort_names(names, scores):
    index = np.argsort(scores)[::-1]
    return names[index]