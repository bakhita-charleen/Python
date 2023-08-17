#if.. elif..else statement
#create a program for grades input with the following
        # 80-100 -A
        #60-79  -B
        #50-59  -C
        #30-49  -D
        #Below 30 -Fail
        # negative and above 100-invalid input
num=int(input("enter the first num:  "))
num2=int(input("Enter the second num:  "))
num3=int(input("Enter the third num:  "))
num4=int(input("Enter the fourth num:  "))

if num>num2 and num2>num3 and num3>num4:
        print(num, "Is greater")
elif num2>num and num2>num3 and num2>num4:
        print(num2, "is greater")
elif num3>num and num3>num2 and num3>num4:
        print(num3, "is greater")
elif num4>num and num4>num2 and num4>num3:
        print(num4, "is greater")
else:
        print("invalid input")