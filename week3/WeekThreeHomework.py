print("Hexagon Week Three Q1")

colorlist = ["red", "green", "blue", "darkred", "cyan", "navy"]

import turtle as tt
tt.title("Q1 Part 1")
tt.width(3)
tt.speed(2)
tt.goto((0,0))

for s in range(6):
    tt.color("black")
    tt.fd(100)
    tt.left(120)
    tt.color(colorlist[s])
    tt.fd(100)
    tt.color("black")
    tt.left(120)
    tt.fd(100)
    tt.left(180)

tt.color("black")
