class calculator:
    def __init__(ref,a,b):
        ref.a=a
        ref.b=b
    def add (ref):
        c=ref.a+ref.b
        print(c)
    def multiply(ref):
        d=ref.a*ref.b
        print(d)
    def divide(ref):
        e=ref.a/ref.b
        print(e)
    def subtratction(ref):
        f=ref.a-ref.b
        print(f)


repe='y'
while repe=='y' or repe=='Y':
    a=int(input("enter the first no"))
    b=int(input("enter the second no"))
    operatin=int(input("enter the operation you want to perform 1.add 2.subtract 3.multiply 4.divide"))
    reef=calculator(a,b)
    if(operatin==1):
        reef.add()
    elif(operatin==2):
        reef.subtratction()
    elif(operatin==3):
        reef.multiply()
    elif (operatin==4):
        reef.divide()
    repe=input("do you want to continue press y or n")
