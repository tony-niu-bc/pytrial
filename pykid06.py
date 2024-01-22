import easygui

mbResult = easygui.msgbox("Hello, Tintin!\nWelcome to the world of GUI")
print("msgbox returns " + mbResult)
print(type(mbResult))

mbResult = easygui.msgbox("I'm a message of messagebox", 
                          "I'm a title of messagebox")
print("msgbox returns " + mbResult)

flavor = easygui.enterbox("what is your favorite thing?", 
                          "Favorite Thing", 
                          "Play Video Game")
easygui.msgbox("your favorite thing is " + flavor)

n = int(float(easygui.enterbox("please input a number", 
                               "be convert integer", 
                               "123.123")))
print(n)

o = float(easygui.enterbox("please input a float number", 
                           "Float", 
                           "99.99"))
print(o)

flavor = easygui.enterbox("what is your favorite game?",
                          default = "zelda")
easygui.msgbox("your entered " + flavor)

f = float (easygui.enterbox("please input a fahrenheit", 
                            default = "37.5"))
c = (5 / 9 )* (f - 32)
easygui.msgbox("celsius was: " + str(c))

d = easygui.enterbox("please input your name: ", 
                     "First name", 
                     "Tintin")
e = int(easygui.enterbox("please input your house number: ", 
                         "House Number", 
                         "123"))
f = easygui.enterbox("please input your city: ", 
                     "City", 
                     "Vancouver")
g = easygui.enterbox("please input your province: ", 
                     "Province", 
                     "BC")
h = easygui.enterbox("please input your postal code: ", 
                     "Postal Code", 
                     "A1B 2C3")

easygui.msgbox("your name is "             + str(d) + 
               " , your house number is "  + str(e) + 
               " ,your city is "           + str(f) + 
               " ,your province is "       + str(g) + 
               " and your postal code is " + str(h) + 
               ".")

easygui.msgbox(str(d) + '\n' +  
               str(e) + '\n' + 
               str(f) + '\n' + 
               str(g) + '\n' +  
               str(h))
