#a = [1, 2, 3, 4, 4, 5, 6, 7]
#
#[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 4] [1, 2, 3, 4, 4, 5] [1, 2, 3, 4, 4, 6] [1, 2, 3, 4, 4, 5, 6, 7]


a = [1, 2, 3, 4, 4, 5, 6, 7]

def combination(org_list):
    list_i = 0
    out_list = [[]]
    tmp_list = []
    while list_i < len(org_list):
        tmp_list.append(org_list[list_i])
        out_list = out_list + [tmp_list[:]]
        list_i = list_i + 1

    return out_list

print(combination(a))






