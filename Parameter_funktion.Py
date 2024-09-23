
def parameter_funk(param1=None, param2=None, param3=None) :

    if param1 == None:
        param1 = "Standartwert"
    if param2 == None:
        param2 = 100
    if  param3 == None:
        param3 = [1, 2, 3]

    print(param1)
    print(param2)
    print(param3)


parameter_funk()

parameter_funk(param1=" meine Variabeln",param2 = 75 )
parameter_funk(param3 = [250,200,175])
parameter_funk("text", [121,111,101])
parameter_funk()

