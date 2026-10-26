# Typecasting: Type conversion, channging datatype

# 1. implicit typecast: compatibility match python datatype convert
# 2. explicit typecast: manually process of changing datatype

# a = 50
# print((type(a)))

# convert to string: - str()
# b = str(a)  # creates a new object from the given object , gives output as "50"
# print(type(b))
# b = "abc" # doesnt work because value not compatible

# convert to integer - int()
# c = int(b)  # 50
# print(type(c))

# convert to float - float()
# d = float(c)  # integer to float
# print(type(d))

# ----

# 1. convert to list
a = "ConvertConvert"  # from string , nnnumbers nnot convertable
my_list = list(a)  # output in []
print(my_list)

# 2. convert to tuple - tuple()
my_tuple = tuple(my_list)
print(my_tuple)  # output in ()

# 3. convert to set
my_set = set(my_tuple)  # only unique datas and unordered
print(my_set)

# 4. convert to dictionary - dict() , cant convert single data to dictionary bc u need key and value (2 datas)
b = [("name", "ram"), ("age", "25")]
my_dict = dict(b)
print(my_dict)

# boolean
a = 1

my_bool = bool(a)
print(my_bool)


#indexing and slicing