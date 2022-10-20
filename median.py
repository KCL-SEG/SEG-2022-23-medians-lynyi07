"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def get_median(ls): 
    sorted_list = ls.sort(); 
    if len(ls) % 2 !=0: 
        position = int ((len(ls)+1)/2-1)
        return ls[position]
    else: 
        position1 = int(len(ls)/2 - 1)
        position2 = int(len(ls)/2)
        return (ls[position1]+ls[position2])/2
        

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(get_median(numbers))
