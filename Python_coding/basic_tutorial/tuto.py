name = "noble man"
age = 20
rg = range(10)
strings = ["my", "world", "apple", "pear"]
numbers = {1, 4, 5, 23, 2}
summation = sum(numbers)
iter_nums = {4, 5, 2, 3, -1, 0, 9}
sorted_nums = sorted(iter_nums, reverse=True)

def longer_than_4(string):
    return len(string) > 4

filtered = filter(longer_than_4, strings)
    

def return_length(string):
    item_length = []
    for i in string:
        item_length.append(len(i))
    return item_length

lengths = map(len, strings)
    
print("My name is", name, end=' | ')
print("I am", age, "years old")
print(list(rg))
print(return_length(strings))
print(list(lengths))
print(list(filtered))
print(summation)
print(sorted_nums)
