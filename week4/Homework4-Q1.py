colorlist = ("red","orange","green","cyan","navy","purple")

import turtle as tt

tt.title("Q1")

tt.width(2)
for a in range(20):
    tt.color(colorlist[a%6])
    tt.penup(); tt.back(50); tt.pendown()
    tt.fd(100)
    tt.penup(); tt.back(50); tt.pendown()
    tt.left(18)
    tt.penup(); tt.fd(10); tt.pendown()

tt.hideturtle()
