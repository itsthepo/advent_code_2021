#import the list
txtfile=open("C:\\Users\\Wolfy\\code\\advent_code_2021\\day1_sonar_sweep\\input.txt", encoding='UTF-16')
L=[]
for line in txtfile:
    L.append(line.rstrip())
L = (list(map(int, L)))


# Make a counter to count the number of times a depth measurement
# sum increases from the previous 3-number sum.
# Also make a blank variable called 'prev_sum'
counter = 0
prev_sum = None

# Loop over numbers array with index:
for i, number in enumerate(L): 
    # Skip if it's the first or second number (Start loop at the 3rd number)
    if i != 0 and i != 1: 
        # Calculate the sum of the 3 numbers
        sum = number + L[i-1] + L[i-2]
        # Add to the counter if the sum is greater than the previous sum (and the prev_sum is not none)
        if prev_sum and sum > prev_sum: 
            counter+=1
        # Assign prev_sum to the value of sum for the next loop:
        prev_sum = sum

# Display solution in the terminal:
print(f"The solution is: {counter}")
