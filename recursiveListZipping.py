def convert_to_list(stuffs):
    list_of_stuff = []
    for left in stuffs:
        if isinstance(left, int):
            list_of_stuff.append([left])
        else:
            list_of_stuff.append(left)
    return list_of_stuff
        
def has_one_item(lst):
    if len(lst) == 1:
        for elem in lst:
            if isinstance(elem, list):
                # Recursively check if the sublist has one item
                if has_one_item(elem):
                    return True
            else:
                # Check if the list has one item
                if len(lst) == 1:
                    return True
                else:
                    return False
    # If none of the elements are lists with one item or the list itself has one item, return False
    return False

def recursive_zip(left, right):
    if isinstance(left, list) and isinstance(right, list):
        left = convert_to_list(left)
        right = convert_to_list(right)
        #print("unzip", left, right)
        # both values are lists, so zip them recursively
        return [(l, r) for l, r in zip(left, right)]
    else:
        # one or both values are not lists, so return them as a tuple
        return (left, right)

def compare(left, right):
    #print("start", left, right)
    if isinstance(left, int) and isinstance(right, int):
        #print("int", left, right)
        # both values are integers, so compare them directly
        #print((left, "<=", right) if left <= right else (left, ">", right))
        return left <= right
    elif isinstance(left, list) and isinstance(right, list):
        #print("lists", left, right)
        #print("ziiped", list(zip(left, right)), len(list(zip(left, right))))
        # both values are lists, so compare them item by item
        sub_results = []
        if len(list(zip(left, right))) == 0:
            return False
        for l, r in zip(left, right):
            #print("zip", l, r)
            result = compare(l, r)
            if result:
                #print("true", l, r)
                
                # left value is lower, so return True
                sub_results.append(True)
            elif result is False:
                #print("false", l, r)
                # right value is lower, so return False
                sub_results.append(False)
        #return result
        # all items were equal, so return False
        return result if result else False
    
    else:
        #print("convert", left, right)
        # one value is an integer and the other is a list, so convert the integer to a list and try again
        if isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]
        if has_one_item(left) or has_one_item(right):
            print("left", left, "right", right)
            return compare(left, right)
            
        else:
            return compare(left, right)

def do_checks(input):
    print(input)
    if len(input[0]) > len(input[1]):
            return False
    
    resultslist = []
    leftone = len(input[0]) if (len(input[0]) > len(input[1])) else len(input[1])
    for x in range(leftone):
        try:
            resultslist.append(compare(input[0][x], input[1][x]))
        except IndexError:
            return False if len(input[0]) > len(input[1]) else True
    
    return False if False in resultslist else True

inputs = open("d13_examples.txt").read().split("\n\n")
for input in inputs:
    left, right = input.split("\n")
    right = right.strip(']').strip("[").split(',')
    right = [int(x) for x in right]
    left = left.strip(']').strip("[").split(',')
    left = [int(x) for x in left]
   
    #left = left.split(",")
    print(left)
    #right = right.strip('][').split(', ')
    
    print(do_checks([left, right]))