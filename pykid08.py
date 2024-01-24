
for i in range(1, 6) :
    print("hi")
    
for d in range(1, 6, 2) :
    print("hi,tin")

for o in range(1, 6, 2) :
    print(o)

while 3==3 :
    mu = int(float(input("please input a number: "))) 
    if mu == 10 :
        break
    elif mu == 1 :
        print("'1*1 = 1'\n'1*2 = 2'\n'1*3 = 3'\n'1*4 = 4'\n'1*5 = 5'\n'1*6 = 6'\n'1*7 = 7'\n'1*8 = 8'\n'1*9 = 9'")
    elif mu == 2 :
        print("'2*1 = 2'\n'2*2 = 4'\n'2*3 =6'\n'2*4 = 8'\n'2*5 = 10'\n'2*6 = 12'\n'2*7 = 14'\n'2*8 = 16'\n'2*9 = 18'")
    elif mu == 3 :
        print("'3*1 = 3'\n'3*2 = 6'\n'3*3 = 9'\n'3*4 = 12'\n'3*5 = 15'\n'3*6 = 18'\n'3*7 = 21'\n'3*8 = 24'\n'3*9 = 27'")
    elif mu == 4 :
        print("'4*1 = 4'\n'4*2 = 8'\n'4*3 = 12'\n'4*4 = 16'\n'4*5 = 20'\n'4*6 = 24'\n'4*7 = 28'\n'4*8 = 32'\n'4*9 = 36'")
    elif mu == 5 :
        print("'5*1 = 5'\n'5*2 = 10'\n'5*3 = 15'\n'5*4 = 20'\n'5*5 = 25'\n'5*6 = 30'\n'5*7 = 35'\n'5*8 = 40'\n'5*9 = 45'")
    elif mu == 6 :
        print("'6*1 = 6'\n'6*2 = 12'\n'6*3 = 18'\n'6*4 = 24'\n'6*5 = 30'\n'6*6 = 36'\n'6*7 = 42'\n'6*8 = 48'\n'6*9 = 54'")
    elif mu == 7 :
        print("'7*1 = 7'\n'7*2 = 14'\n'7*3 = 21'\n'7*4 = 28'\n'7*5 = 35'\n'7*6 = 42'\n'7*7 = 49'\n'7*8 = 56'\n'7*9 = 63'")
    elif mu == 8 :
        print("'8*1 = 8'\n'8*2 = 16'\n'8*3 = 24'\n'8*4 = 32'\n'8*5 = 40'\n'8*6 = 48'\n'8*7 = 56'\n'8*8 = 64'\n'8*9 = 72'")
    else:
        print("'9*1 = 9'\n'9*2 = 18'\n'9*3 = 27'\n'9*4 = 36'\n'9*5 = 45'\n'9*6 = 54'\n'9*7 = 63'\n'9*8 = 72'\n'9*9 = 81'")
        
num = int(float(input("please input a number: ")))
dn = int(float(input("please input a number that is you want to time: ")))
print(num * dn)

number = int(input("input a number: "))
limit = int(input("how high do you want:"))
print("here is your table: ")
for i in range (1, limit + 1) :
    print(number, "time", i, "=", number * i)