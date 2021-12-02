from os import X_OK


x = 0 
y = 0

def move_sub(direction, coord):
    global x 
    global y
    if direction == "forward":
        x = x + coord
    if direction == "up":
        y = y - coord
    if direction == "down":
        y = y + coord



# import the data 
txtfile=open(".\\input.txt")
L=[]
for line in txtfile:
    line=line.strip()
    line=line.split(" ")
    direction=line[0]
    coord=int(line[1])
    move_sub(direction,coord)

print(x * y)
    


       
