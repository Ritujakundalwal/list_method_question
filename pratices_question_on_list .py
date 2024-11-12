# 1.append
# append ferrari to the list.
cars=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars.append("ferrari")
print(cars)

# 2.insert
# problem statement:insert "porsche" at index 3
cars.insert(3,"porsche")
print(cars)

# 3.clear
# problem Statement:clear all the element to the list.
cars.clear()
print(cars)

# 4.sort
# problem statement:sort the original list of cars in alphabetic order
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.sort()
print(cars1)

# 5.remove
# problem staement:remove audi from the list.
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.remove("audi")
print(cars1)

# 6.Index
# problem Staement: find the index of "mustang"
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
print(cars1.index("mustang"))

# 7.extend
# problem staement:extend the list with the another list and print it
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.extend([11,22,33,])
print(cars1)

# 8.pop
# problem Statement:pop the last element from the list and print it.
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.pop()
print(cars1)


# 9.count
# problem statement:count how many times "bmw "appears in the list.
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
print(cars1.count("bmw"))

# 10.append multiple
# problem statement:append multiple cars:["jaguar","fiat"] to the list.
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.append(["jaguar","fiat"])
print(cars1)

# 11.insert multiple
# problem staement: insert multiple cars ["volvo","honda"] at index 2
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.insert(2,["volvo","honda"])
print(cars1)

#12. clear if empty
# problem staement: check if the list is empty and clear it if it is .
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
if not cars1:
    cars1.clear()
print(cars1)


#13.sort descending
# problem satement: sort the original list of cars in descending order.
cars1=["bmw","mahindra","suzuki","rolls royce","bentley","aston martin","tata","audi","mustang"]
cars1.sort(reverse=True)
print(cars1)

# 14.remove all occurance
# problem staement:remove all occurance of "bmw" from the list.
cars1 = ["bmw", "mahindra", "suzuki", "rolls royce", "bentley", "aston martin", "tata", "audi", "mustang"]
cars1 = [car for car in cars1 if car != "bmw"]
print(cars1)

# 15.find last index
# problem staement: find the last index of "tata"
cars1 = ["bmw", "mahindra", "suzuki", "rolls royce", "bentley", "aston martin", "tata", "audi", "mustang"]


# 16.extend with condition
# problem staement: extend the list with["ferrari","lambo"] only if "bmw" is in the list.
cars1 = ["bmw", "mahindra", "suzuki", "rolls royce", "bentley", "aston martin", "tata", "audi", "mustang"]
if "bmw" in cars1:
    cars1.extend(["ferrari", "lambo"])
print(cars1)
