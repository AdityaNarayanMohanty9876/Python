# print("Hello world")
# print("Aditya mohanty, My age is 23")
# print(23)
# print(23+35)

# finding out type
# name = "Aditya Narayan Mohanty" 
# age = 23
# price = 25.99
# print(name,age,price)
# print(type(name))
# print(type(age))
# print(type(price))

# finding out type none and boolean
# age = 23
# old = False
# a = None
# print(type(old))
# print(type(a))

# a = 2 
# b = 5
# sum = a+b
# print(sum)

# Taking user or input keyboard
# name = input("name: ")
# age = int(input("age: "))
# price = float(input("price: "))
# print(name, age, price)

# conditional statement
# age = int(input("age: "))
# if(age<18):
#     print("Can't vote")
# else:
#     print("Can vote")    

# lights = input("lights: ")
# if(lights == "red"):
#     print("Stop")
# elif(lights == "yellow" ):
#      print("Wait")   
# elif(lights == "green"):
#      print("go")
# else:
#      print("invalid statement")           

# marks = int(input("marks: "))
# if(marks>90):
#     print("O GRADE")
# elif(marks>80 and marks<90):
#     print("A GRADE")
# elif(marks>70 and marks<80):
#     print("B GRADE")
# else:
#     print("fail")        

# Ternary operator, conditional statement in one line
# food = input("food: ")
# eat = "yes" if food == "cake" else "no"
# print (eat)
 
age = int(input("age: "))
vote = "Can vote" if age >= 18 else "cannot vote"
print(vote)