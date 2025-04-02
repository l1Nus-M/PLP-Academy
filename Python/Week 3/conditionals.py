
temperature = input("Enter temperature: ")
temperature = int(temperature)

if temperature >= 30:
    print("It's a hot day")

print("This is a grading program!")

grade = input("Enter your grade: ")
grade = float(grade)

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
else:
    print("You got an F!")
