


def find_sec_largest(lst):
    frst_larg = lst[0]
    sec_larg = lst[0]

    for i in range(1, len(lst)):
        
        if lst[i] > frst_larg:
            sec_larg = frst_larg
            frst_larg = lst[i]

        elif lst[i] > sec_larg:
            sec_larg = lst[i]

    return frst_larg, sec_larg

lsts = [5, 4, 3, 345, 644, 643, 64, 5]
print(find_sec_largest(lsts))

# this technology has some problem, that is, if the first element of the list is the biggest number, this program will not work properly. 