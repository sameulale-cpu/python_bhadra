# Exception handling: 
# exception raise line place it in try block place  
# except block: statements to be executed when case of exception 
# can define multiple error specific except block
# can have one one catch all except 

#try:
#    statement
#except:
#    statement
try:    #(if no error arise try works, if some error arise , goes to exception) e.g. a = abc
    a = int(input("enter a number:"))
    print(a + 10) # if b instead of a it prints name error
except ValueError:
    print("Value error")
except NameError:
    print("name error")

except: #catches all errors, only one can't get 2 of these
    print("All error")

#calculator implement exception handling , mark evaluator