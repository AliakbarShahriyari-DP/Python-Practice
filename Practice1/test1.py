# print("Hello World!");


# For :: مجموع اعداد زوج 

# total = 0

# for i in range(1, 11):
#     if i % 2 == 0:
#         total += i

# print("Sum of even numbers:", total)


# شمارش معکوس از 1 تا 100 

# number = 100

# while number >= 1:
#     print(number)
#     number -= 1

# print("Finished!")

#رسم مثلث 

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

size = 10

for i in range(0,size):
    print(" " * (size - i), end=" ")
    print("* " * i, end=" ")
    print()