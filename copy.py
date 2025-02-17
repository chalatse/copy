import copy

original = [1, [1,2]]
deep_copy = copy.deepcopy(original)

deep_copy[0] = 100 
deep_copy[1].append(4)

print(original)
print(deep_copy)

