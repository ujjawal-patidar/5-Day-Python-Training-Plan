# Use itertools.combinations to find all possible pairs from a list and filter pairs that sum to a target value.

from itertools import combinations

def func(l, target_sum):
    ans = []
    for i, j in combinations(l, r = 2):
        if(i + j == target_sum):
            ans.append((i, j))
    return ans

print(func([1,2,3,4], 5))
print(combinations([1,2,3,4], r = 2))

# for i, j in combinations([1,2,3,4], r = 2):
#     print(i, j)