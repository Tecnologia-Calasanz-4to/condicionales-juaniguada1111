def suma(n1,n2):
    r = n1+n2
    return r
def resta(n1,n2):
    r = n1-n2
    return r
def multiplicacion(n1,n2):
    r = n1*n2
    return r
def division(n1,n2):
    r = n1/n2
    return r
def main():
    print("ingrese un numero")
    n1=float(input("ingrese n1"))
    n2= float(input("ingrese n2"))
    print("1-suma")
    print("2-resta")
    print("3-multiplicacion")
    print("4-division")
    opcion = int(input("dame opcion"))

    if opcion==1:
        print (suma(n1,n2))
    elif opcion==2:
        print (resta(n1,n2))
    elif opcion==3:
        print(multiplicacion(n1,n2))
    elif opcion==4:
        print(division(n1,n2))
    return 
main() 
          
