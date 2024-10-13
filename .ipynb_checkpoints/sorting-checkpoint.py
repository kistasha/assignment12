# defining the method
def sorting_tool(integers_list):
    #first, determining the length of the list
    n = len(integers_list)
    
    
    # starting the outer for loop to go through each element in the list
    for i in range (n):
        # nesting another for loop to compare elements
        # this loop will only run until n-i-1 instead of n,
        # since last i elements are already sorted
        for k in range(0,n-i-1):
            if integers_list[k] > integers_list[k+1]:
                # swap the values if needed
                integers_list[k],integers_list[k+1] = integers_list[k+1],integers_list[k]
                
    return integers_list


# Testing the custom method
test1 = [1,5,4,3,6,7,7]
test2 = [4,-1,0,1,435,-12,32,324,-12,-243,342,56,8,0,0,222,5677]

test1_sorted = sorting_tool(test1)

test2_sorted = sorting_tool(test2)

print()
print(f'List 1 sorted: {test1_sorted}\nList 2 sorted: {test2_sorted}')
print()


