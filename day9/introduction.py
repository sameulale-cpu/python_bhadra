# create a function that prints out the introduction of the user 
# get name, address and other detailse from user that can be used for introduction

Name = input("Enter name:")
Address = input("Enter address:")
Age = int(input("Enter Age:"))

def introduce(name, address, age):
    print(f"""Name = {name}
Address = {address}
Age = {age} """)

introduce(Name, Address, Age)