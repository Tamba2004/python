my_list = [1, 2, 3, "hello", 4.5, True]
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: hello
print(my_list[5])  # Output: True
print(my_list[-1])  # Output: True
print(my_list[-2])  # Output: 4.5
print(my_list[-3])  # Output: "hello"

print(my_list[1:4])  # Output: [2, 3, "hello"]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[3:6])  # Output: ["hello", 4.5, True]
print(my_list[::2])  # Output: [1, 3, 4.5]


chaine = "Bonjour,comment ça va ?"
print(chaine[0])  # Output: B
print(chaine[8])  # Output: c
print(chaine[-1])  # Output: ?

my_list_1 = [1, 2, 3, "world", 5]
my_list_1[1] = "Python"
my_list_1.append(6)
my_list_1.remove(3)
my_list_1.insert(2, "new")



print(my_list_1) 

print(my_list_1 + my_list)  # Output: [1, 'Python', 'new', 'world', 5, 6, 1, 2, 3, 'hello', 4.5, True]