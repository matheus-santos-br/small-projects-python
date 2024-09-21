def find_index(list, value):

    c = 0

    for item in list:
        if(item == value):
            print(F"Position {c}")
            return
        
        c+=1

def list_slicer(list, start, end):
    new_list = list[start:end]
    return new_list

find_index([4,3,2,1,0],0) #Position 4

sliced_list1 = list_slicer([4,3,2,1,0], 2, 4)
sliced_list2 = list_slicer([4,3,2,1,0], 0, 3)

print(sliced_list1) # [2, 1]
print(sliced_list2) # [4, 3, 2]