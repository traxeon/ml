"""Calculates math curves for mean functions of student scores"""
import math
import numpy as np


def flat_curve(arr, val):   # function, accepts an array
    """Calculates a flat curve against an array of values"""
    return [i + val for i in arr]

def sqrt_curve(arr):   # function, accepts an array
    """Calculates a square root curve against an array of values"""
    return [math.sqrt(i) * 10 for i in arr]

# call the function
test_scores = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_scores, 5)
curved_10 = flat_curve(test_scores, 10)
curved_sqrt = sqrt_curve(test_scores)

for score_list in test_scores, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))
