colorlist = ("red","orange","green","cyan","navy","purple")

import turtle as tt

tt.title("Q2")

for a in range(20):
    for b in range(6):
        tt.width((6-b)/2)
        tt.color( colorlist[b] )
        tt.fd(30)
    tt.penup(); tt.back(80); tt.pendown()
    tt.left(18)
    tt.penup(); tt.back(75); tt.pendown()

tt.hideturtle()
