#Method 1 Concatenation
name = "Arun"
name1 ="Alagaraj"
print(name+" "+name1)

#method 2 C-style format
name ="Arun"
age = 21
score = 100
print("%s is age is %d and he score a %d"%(name,age,score))

#Method 3  .format
name ="Arun"
age1 = 21
score = 100
print("{} is age is {} and he was scored a {}".format(name, age1, score))


#Method 3  f'string
name ="Arun"
age2 = 20
score = 100
print(f"{name} age is{age2} and he was score a{score} ")