tedad_win = 0
point_t = 0

for i in range(0,30):
    points = int(input ())
    if points> 3 :
        print("Less than four")
        continue
    if points  == 2 :
        print("2 impossible")
        continue
    if points ==3 :
        tedad_win+=1

    if points==3 :
        point_t+=3
    elif points == 1:
        point_t+=1
    elif points == 0 :
        point_t += 0
print (str(point_t)+" "+str(tedad_win))

