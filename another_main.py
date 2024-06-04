# Variables
#snake_case for python variables
#camelCase for Javascript
#PascalCase for classes in all the languages
#kebab-case not applied in programming

num1 = 5
num2 = 7

print(num1 + num2)

num2 = 1

print(num1 + num2)
# assign the value of num2 to num1
# num1 <- num2
num1 = num2
print(num1 + num2)

num3 = 5

num3 = num3 + 2
print(num3)

num3+= 3 #num3 = num3 + 3
print(num3)
total = num1 + num2 + num3

# String interpolation

print("The total addition is", total)
print(f"The total addition is {total}")