def Type_name(var1):
    return type(var1)



print(Type_name(21))  
print(Type_name(30.5))  
print(Type_name("Welt")) 
print(Type_name([1, 2, 3]))
print(Type_name((1, 2, 3)))  
print(Type_name({1, 2, 3})) 
print(Type_name({"x": 1}))
print(Type_name(True))    
print(Type_name(None))   


import math

x = math.floor(1.4)
y = math.ceil(1.4)
print(x) 
print(y) 
x = math.pi
print(x)



rest = 15.2 % 3.6
print(rest)