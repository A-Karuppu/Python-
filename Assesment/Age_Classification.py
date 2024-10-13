def classify_age():
    age = int(input("Enter your age: "))
    if age < 0:
        print("Invalid age")
    elif age < 18:
        print("Minorr")
    elif age >= 18 and age < 60:
        print("Adult")
    else:
        print("senior citizen")


classify_age()