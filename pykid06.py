import easygui
d =  easygui.enterbox("please input your name .")
e = float(easygui.enterbox("house number ."))
f = easygui.enterbox("city.")
g = easygui.enterbox("province.")
h = float(easygui.enterbox("postal code."))
ho = str(d) + '\n' +  str(e) + '\n' + str(f) + '\n' + str(g) + '\n' +  str(h) 
easygui.msgbox(ho) 

import easygui

mbResult = easygui.msgbox("Hello, Tintin!\nWelcome to the world of GUI")
print("msgbox returns " + mbResult)
print(type(mbResult))

mbResult = easygui.msgbox("I'm a message of messagebox", 
                          "I'm a title of messagebox")
print("msgbox returns " + mbResult)

import easygui
flavor = easygui.enterbox("what is your favorite thing?")
easygui.msgbox("your favorite thing is " + flavor)

n = int(float(easygui.enterbox("please input a number")))
print(n)

o = float(easygui.enterbox("please input a number"))
print(o)

import easygui 
flavor = easygui.enterbox("what is your favorite game?",
                           default = "zelda")
easygui.msgbox("your entered " + flavor)

f = float (easygui.enterbox("please input a fahrenheit"))
c = (5 / 9 )* (f - 32)
easygui.msgbox("it was" + str(c))

import easygui
d =  easygui.enterbox("please input your name .")
e = float(easygui.enterbox("house number ."))
f = easygui.enterbox("city.")
g = easygui.enterbox("province.")
h = float(easygui.enterbox("postal code."))
easygui.msgbox("your name is "             + str(d) + 
               " , your house number is "  + str(e) + 
               " ,your city is "           + str(f) + 
               " ,your province is "       + str(g) + 
               " and your postal code is " + str(h) + 
               " .")

import easygui
d =  easygui.enterbox("please input your name .")
e = float(easygui.enterbox("house number ."))
f = easygui.enterbox("city.")
g = easygui.enterbox("province.")
h = float(easygui.enterbox("postal code."))
ho = d + '/n' + e + '/n' + f + '/n' + g + '/n' + h +'/n'
easygui.msgbox(ho) 