store = {};
target = 9;
num = [2,7,11,15];

for val in num:
    if val in store:
        print([val, store[val]]);
    store[target - val] = val
