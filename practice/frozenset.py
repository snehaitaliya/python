#frozenset
# x=frozenset({"apple","banana","cherry"})
# print(x)
# print(type(x))

#copy
# fs = frozenset({1, 2, 3})
# cp = fs.copy()
# print(fs)
# print(cp)

#difference
# a = frozenset({1, 2, 3, 4})
# b = frozenset({3, 4, 5})
# print(a.difference(b))
# print(a - b)

#intersection
# a = frozenset({1, 2, 3, 4})
# b = frozenset({3, 4, 5})
# print(a.intersection(b))
# print(a & b)


#isdisjoint
# a = frozenset({1, 2})
# b = frozenset({3, 4})
# c = frozenset({2, 3})
# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

#issubset
# a = frozenset({1, 2})
# b = frozenset({1, 2, 3})
# print(a.issubset(b))
# print(a <= b)
# print(a < b)

#issuperset
# a = frozenset({1, 2, 3})
# b = frozenset({1, 2})
# print(a.issuperset(b))
# print(a >= b)
# print(a > b)

#symmetric_difference
# a = frozenset({1, 2, 3})
# b = frozenset({3, 4, 5})
# print(a.symmetric_difference(b))
# print(a ^ b)

#union
# a = frozenset({1, 2})
# b = frozenset({2, 3})
# print(a.union(b))
# print(a | b)

#--------------------------------------------------------------------------------

#setmethod

#add
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)

#clear
# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)

#copy
# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)

#diff
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# z1=y.difference(x)
# print(z^z1)
# print(z)
# #print(z1)

#diff_update
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y)
# print(x)

#discard
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)

#INTERSECTION
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)

#intersection_update
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

#isdisjoint
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z)

#subset
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)

#issuperset
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)

#pop
# fruits = {"apple", "banana", "cherry"}
# fruits.pop()
# print(fruits)

#remove
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)

#
