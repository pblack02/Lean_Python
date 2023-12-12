# If Statements
if 1<2:
    print("First Statement")
    if 20 < 3:
        print("Second Statement")

# IF-else Statement
if 10 < 6:
    print("Hello")
elif 3 == 3:
    print('ELIF ran')
else:
    print("GoodBye")

# For Loops
seq = [1,2,3,4,5,6,7,8]

for item in seq:
    # Code Here
    print(item)

# For loops with tuples
my_pairs= [(1,2),(3,4),(5,6)]

for pair in my_pairs:
    print(pair)

    # Tuple unpacking
for (tup1, tup2) in my_pairs:
    print(tup1, tup2)

# While loops
i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i + 1

# range() > Auto generates a list for you
for item in range(10):
    print(item)

# List Comprehension
x = [1,2,3,4,5,6]
# out = []
# for num in x:
#     out.append(num**2)
# print(out)
out = [num**2 for num in x]
print(out)


