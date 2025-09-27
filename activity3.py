mark1=int(input("Enter your marks"))
mark2=int(input("Enter your marks"))
mark3=int(input("Enter your marks"))
mark4=int(input("Enter your marks"))
mark5=int(input("Enter your marks"))
average=mark1+mark2+mark3+mark4+mark5/5
if average>=91 and average<100:
    print("A1")
elif average>=81 and average<91:
    print("A2")
elif average>=71 and average<81:
    print("B1")
elif average>=61 and average<71:
    print("B2")
elif average>=51 and average<61:
    print("C1")
elif average>=41 and average<51:
    print("C2")
else:
    print("you hve failed")