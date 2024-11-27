my_dict={'комната 1':5,"комната 2":76,"комната 3":39}
print(my_dict)
print(my_dict.get("комната 3"))
print(my_dict.get("комната 4"))
my_dict.update({"комната 4":51,"комната 5":38})
a=my_dict.pop("комната 1")
print(a)
print(my_dict)
my_set={1,5,9,"воздух","аллея",True,False,"воздух","сорока",5,8,9,False,"аллея"}
print(my_set)
print(my_set.add("принц"))
print(my_set.add(69))
print(my_set.discard("аллея"))
print(my_set)