def add(num1,num2):
    sum = num1 + num2
    return sum
print(add(3, 4))

print("***************************************")
#Keyword Arguments

def add(num1,num2):
    sum = num1 + num2
    return sum

result=add(num2=5,num1=6)
print(result)

print("****************************************")


#Arbitary Arguments  or  Args

def add(*nums):
    return sum(nums)

result2=add(10,20,40,56,476)
print(result2)

print("****************************************")

#Keyword Arbitary Arguments  or  kwargs
def laptop(**Values):
    print(Values)
laptop(
    name="Asus",count=100,
    name1="Dell", count1=50,
    name2="HP", count2=13,
    name3="Mac",count3= 12,
)
