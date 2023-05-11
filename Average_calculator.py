total=0
courses=[]
num_of_numbers=int(input("Enter the number that you want calculate:"))
for i in range(num_of_numbers):
    courses.append(float(input("Enter a number:")))
total=sum(courses)/num_of_numbers
print(total)
