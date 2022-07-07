# # set
# set1 = set(range(2))
# set2 = set(range(0, 4))
# set1 = set1.union(set2)
# set1.add(5)
# # set1.clear()
# set1.symmetric_difference_update(set2)
# print(set1.difference(set2), set1.symmetric_difference(set2), )
# print(set1)

a = [1, 2, 3, 4, ]
b = [5, 6, 7, 1, ]
c = set(a)
d = set(b)
print(c.intersection(d))
print(c.issuperset(d))

