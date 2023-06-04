the_list = [10,15,3,7]
k = 17

def day_one(the_list : list, k : int) -> bool :
    the_flag = False
    break_first_loop = False
    for index in range(0, len(the_list)):
        for index2 in range(index, len(the_list)):
            if(the_list[index] + the_list[index2] == k):
                the_flag = True
                break_first_loop = True
                break
            else:
                the_flag = False
        if(break_first_loop):
            break
    return the_flag

def day_one_single_pass(the_list: list, k : int) -> bool:
    the_flag = False
    for index in range(0, len(the_list)):
        num_complement = k - the_list[index]
        if(num_complement in the_list):
            the_flag = True
            break
        else:
            the_flag = False
    return the_flag

print(day_one(the_list, k))
print(day_one_single_pass(the_list, k))