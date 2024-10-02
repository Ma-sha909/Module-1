#словари
my_dict={"Вася":1994, "Марина":1990, "Никита":2001}
print(my_dict)
print(my_dict["Марина"])
print(my_dict.get("LOL"))
my_dict.update({"Миша":2004, "Аня":1999})
print(my_dict)
f = my_dict.pop("Вася")
print(f)
print(my_dict)
#множества
my_set={1,3,"h","comp",02.10}
print(my_set)
print(my_set.update("8","6"))
print(my_set)
my_set.remove(02.10)
print(my_set)