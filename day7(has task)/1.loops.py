# Loop: Iteration -> execute a task/block of code multiple time

# while loop: boolean data based
# based on condition
# if the given condition is true , while block is executed, otherwise block not executed
# while block-> statement

# statement
# while condition(True/False):
#    statement1
#    statement2
#    statement3
# statement4

a = 0
b = 5
# while a < b:
#    if a == 2:  # prints hello 2 times and prints end of loop
#        break
#    print("hello")
#    a += 1  # a = 1,2,... prints hello 5 times
# print("End of loop")

# break: loop end line(line 19- 22)
# continue: skip the current loop and start the new loop(line 27-30)

# while a < b:
#    a += 1
#    if a == 2:  # when a == 2(True) it goes up(a(2) < b(5)) and a = 2 + 1 = 3 so skips hello 2 in output, prints end of loop as well in last
#        continue
#    print("hello", a)
# print("End of loop")

a = "15"
print("Hello", 10)
print("Hello" + a)  # can only concatenate string not other

name = "dia"
age = 30
address = "kathmandu"
print("hello i am", name, "I am", age, "years old. I am from", address)
print(f"hello i am {name} I am {age} years old. I am from {address}")
