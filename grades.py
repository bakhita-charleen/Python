# 80-100 -A
# 60-79  -B
# 50-59  -C
# 30-49  -D
# Below 30 -Fail
# negative and above 100-invalid input

mark=int(input("Enter mark:  "))
#mark2=int(input("Enter the second mark:  "))
#mark3=int(input("Enter the third mark:  "))
#mark4=int(input("Enter the fourth mark:  "))
#mark5=int(input("Enter the fifth mark:  "))
#mark6=int(input("Enter the sixth mark:  "))

if mark>=80 and mark<=100:
        print("A")
elif mark>=60 and mark<=79:
        print("B")
elif mark>=50 and mark<=59:
        print("C")
elif mark>=30 and mark<=49:
        print("D")
elif mark<30:
        print("Fail")
else:
    print("invalid input")
