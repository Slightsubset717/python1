colorlist = ("red","orange","green","cyan","navy","purple")

import turtle as tt
tt.speed(0.1)
tt.title("Q3")

for a in range(20):
    for b in range(6):
        tt.width((6-b)/2)
        tt.color( colorlist[b] )
        tt.fd(30)
    tt.penup(); tt.back(130); tt.pendown()
    tt.left(18)
    tt.penup(); tt.back(30); tt.pendown()

tt.hideturtle()
