# while loop
# write python program to print the first 5 numbers using for loop.

for i in range(5):
    print(i)
# 1 to 10 all even number using for loop
for i in range(1,11):
    if i % 2 ==0:
        print(i)

i = 0 
while i <= 4:
    print(i)
    i += 1   # i = i + 1
#jumping statments
#write a python program to print numbers from 1 to 5, but stop the loop when the number reaches 4
for i in range(1,6):
    if i == 4:
        break
    print(i)

#continue statment
#write the program to print nymbers from 1 to 5, but skip the number 4 using continue
for i in range(1,6):
    if i == 4:
        continue
    print(i)

#pass statment
#write a program using for loop from 1 to 9 and use pass as a placeholder inside the loop
for i in range(1,10):
    pass

#write a program to create a function add() without implementing its logic
def add():
    pass

#return statment
#write a function called square(n) that accespts a number and returns its square
def square(n):
    return n*n
print(square(3))