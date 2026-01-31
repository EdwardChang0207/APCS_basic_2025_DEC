l = [10, 2, 38, 18, 5, 18, 29]
n_min, n_max = l[0], l[0]
for i in l:
    if i > n_max: n_max = i
    if i < n_min: n_min = i
print(f'min:{n_min}, max:{n_max}')