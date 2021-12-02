#set counter
counter = 0

#import the list
txtfile=open("C:\\Users\\Wolfy\\code\\advent_code_2021\\day1_sonar_sweep\\input.txt", encoding='UTF-16')
L=[]
for line in txtfile:
    L.append(line.rstrip())
L = (list(map(int, L)))

##### run the for loop to determine if the previous number is smaller
for i, number in enumerate(L): 
    if i != 0: 
        if number > L[i-1]:
            counter+=1

print(counter)

        