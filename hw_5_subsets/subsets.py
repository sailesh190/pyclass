#list all the subsets of [1, 2, 3, 4, 4, 5, 6, 7]

def sublists(list_to_process):
    
    if list_to_process == []:
        
        return [[]]
    
    first_element = list_to_process[:1]
    
    the_others = list_to_process[1:]
    
    the_others_sublists = sublists(the_others)
    
    return the_others_sublists + [first_element + item for item in the_others_sublists]
 
list_to_process = [1, 2, 3, 4, 4, 5, 6, 7]

desired_sublists = sublists(list_to_process)

print("If repetition is allowed:\n", desired_sublists)

set_of_tuples = set(tuple(item) for item in desired_sublists)

sublists_wo_repetition = [list(item) for item in set_of_tuples]

print("If repetition is not allowed:\n", sublists_wo_repetition)