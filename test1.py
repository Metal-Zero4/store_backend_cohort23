about_me = {
    "name": "Angel",
    "last": "Garcia",
    "age": 26,
    "hobbies": [],
    "address": {
        "street": "4243 Browne",
        "city": "Brownsville"
    }
}

print( about_me["name"] )


print(f"{about_me['name']} {about_me['last']}")

address = about_me["address"]
print(address["street"])
print(address["city"])



# modify
about_me["age"] = 27

# create new key
about_me["phone"] = "123 456 7890"

print(about_me)


# List
print("-" * 40)

names = []
names.append("Gary")
names.append("Oscar")
names.append("Angel")
names.append("Kvon")

print(names)


print(names[0])
print(names[1])
print(names[2])
print(names[3])

# for loop
print("using loops" * 4)
for name in names:
    print(name)


nums = [1,2,3,4,5,6,7,5,4,4,7,2,54,6,2,768,89,345,5467,908,2,4,78,678,123,435]

# exe 1: print all numbers
for num in nums:
    if num != 4:
         print(num)


# exe 2: count how many 4's there are in the list
counter = 0
for num in nums:
    if num == 4:
        counter = counter + 1

print(counter)
print(nums.count(4))





# exe 3: Sum all the nums
"""
sum = 0
for num in nums:
    #sum = sum + num
    
    my_sum += num

print(my_sum)

#shortcut to my method below
print(sum(nums))
"""

sum_of_nums = sum(nums)
print(sum_of_nums)



students = [ 
    {
        "name": "Kvon",
        "age": 36
    },
   {
        "name": "Gary",
        "age": 37
    },
    {
        "name": "Oscar",
        "age": 33
    },
    {
        "name": "Angel",
        "age": 35
    },
]

# exe 4: Sum the ages (141)
total = 0
for student in students:
    age = student["age"]
    total += age

print(total)


# Find the minium algorithm

ages = [ 62,34,21,78,23,88,20, 65,32, 17, 94, 17, 16, 65,21,89
]
min = ages[0]
for num in ages:
    if num < min:
        min = num 
print(f"the youngest person's age is {min}")

from mock_data import catalog
def get_unique_categories():
    print("-" * 30)

    categories = []
    for prod in catalog:
        if prod["category"] not in categories:
            categories.append(prod["category"])
    
    print(categories)


        #print(prod["category"])

get_unique_categories()


colors = ["red", "blue", "orange", "orange", "Blue", "Green", "Red", "blue", "Black", "gray", "GrAY", "oRanGE"]
def get_unique_colors():
    print("*" * 30 )
    result = []
    for uColor in colors:
        if uColor.lower() not in result:
            result.append(uColor.lower())
    print(result)
              

get_unique_colors()