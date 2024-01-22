my_number = 7
if my_number < 20:
    print("Under 20")
else:
    print("20 or over")

my_number = 25
if my_number < 20:
    print("Under 20")
else:
    print("20 or over")

number = float(input("please input a number: "))
if (number > 30) and (number < 40) :
    print("this number is big to 30 and small to 40")
elif number < 30:
    print("it was small to 30")
elif number > 40:
    print("it was big to 40")

l = input ("please input letter: ")
if 'A' <= l <='Z' :
    print("it was upper case")
elif 'a' <= l <='z' :
    print("it was lower case")
else:
    print("it was not letter")

money = float(input("please in put your price: "))
if money > 10 :
    print(money * 0.8)
else:
    print(money * 0.9)

answer = str(input("please in put did you a girl (input yes or no): "))
if "yes" == answer :
    g = float(input("please input how old are you(input number): "))
    if 10 < g < 12 :
        print("you can join the soccer team now")
    else:
        print("sorry you can't join coccer team ")
else:
    print("sorry you can't join the soccer team")

l = float(input("please input your fule tank is how big(liter): "))
p = float(input("now your fule is how many percent : "))
k = float(input("one liter can go how long (kilometer): "))

print(l)
print(p)
print(k)

r = l * (p / 100) - 5
d = r * k
if d > 200 :
    print("you can go to next gas station: ")
else:
    print("you can't go to next gas station")


while "19965" != input("please input a password: ") :
    print("password is wrong") 

print("you're in!")