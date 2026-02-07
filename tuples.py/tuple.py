tuple = ("abdi", "abdul", "abdu", "abdi", 5, True)
print(tuple, len(tuple))

list = tuple
list.append("67")
tuple = tuple(list)
print(tuple)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)               #THIS ONE IS BASICALLY A DICTIONARY BUT IN TUPLE FORM
print(red)


