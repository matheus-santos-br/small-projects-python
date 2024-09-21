# a function that takes a list and taget parameter
# multiple variables: middle, start, end, steps
#recursion or while loop
# increase the steps each time the split is done
# conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 1

    while(start <= end):
        print(F"Step: {str(steps)}:{str(list[start:end+1])}")
        #start += 1
        steps += 1

        middle = (start + end) // 2
        print(middle)
        if (element == list[middle]):

            return middle
        
        if (element < list[middle]):
            end = middle - 1

        else: 
            start = middle + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10]
target = 2

binary_search(my_list,target)
