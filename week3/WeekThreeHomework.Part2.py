print("Hexagon Week Three Q2 Part 2")

colorlist = ["cyan", "navy", "red", "green", "blue", "darkred", "cyan", "navy", "red", "green", "blue", "darkred", "cyan", "navy", "red", "green", "blue", "darkred"]

import turtle as tt
import time as tm
tt.title("Q2 Part2")
tt.speed(2)

for n in range(3, 11):
    for t in range(n):
        tt.color(colorlist[t])
        tt.fd(100)
        tt.left(360/n)
    tm.sleep(2)
    tt.clear()
    

