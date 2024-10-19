num1 = 10
while True:
    try:
        num2=int(input("Enter a number: "))
        break
    except :
        print ("Enter a valid number")


sum=num1+num2
print(sum)

print("==================================================================================")

try:
    a="Arun"+"Hero"
    print(a)
except:
    print("Enter a valid number")

else:
    print("No else error")


print("====================================================================================")

try:
    a="Arun"+"Hero"
    print(a)
except:
    print("Enter a valid number")

else:
    print("No else error")

finally:
    print("No else error")