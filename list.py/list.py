thislist = ["abc", 34, True, 40, "male"]
print(thislist, len(thislist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-5:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("apple is in list")


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = []
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Finding element in list

Cities = ["Astana", "Almaty", "Shymkent", "Aktau", "Taraz"]
for i in range(len(Cities)):
  if Cities[i] == "Shymkent":
    print("Shymkent is", i+1, "city in the list")


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
