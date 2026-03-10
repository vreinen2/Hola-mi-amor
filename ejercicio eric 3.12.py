num1=int(input("Introduce número 1:"))
num2=int(input("Introduce número 2:"))
num3=int(input("Introduce número 3:"))

if num1<num2 and num2<num3:
    print(num1)
    print(num2)
    print(num3)
else:
    if num2<num3 and num3<num1:
        print(num2)
        print(num3)
        print(num1)
    else:
        if num3<num1 and num1<num2:
            print(num3)
            print(num1)
            print(num2)
        else:
            if num1<num3 and num3<num2:
                print(num1)
                print(num3)
                print(num2)
            else:
                if num2<num1 and num1<num3:
                    print(num2)
                    print(num1)
                    print(num3)
                else:
                    if num3<num2 and num2<num1:
                        print(num3)
                        print(num2)
                        print(num1)
                    
        