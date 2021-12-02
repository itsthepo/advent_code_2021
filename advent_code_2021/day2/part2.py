x = 0 
y = 0
aim = 0

def move_sub(direction, coord):
    global x 
    global y
    global aim
    if direction == "forward":
        x = x + coord
        y = (aim * coord) + y 
    if direction == "up":
        aim = aim - coord
    if direction == "down":
        aim = aim + coord
        



# import the data 
txtfile=open("C:\\Users\\Wolfy\\code\\advent_code_2021\\day2\\input.txt")
for line in txtfile:
    line=line.strip()
    line=line.split(" ")
    direction=line[0]
    coord=int(line[1])
    move_sub(direction,coord)

print(x * y)
    


       
