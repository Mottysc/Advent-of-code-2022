def convert_to_list(stuffs):
    list_of_stuff = []
    for left in stuffs:
        if isinstance(left, int):
            list_of_stuff.append([left])
        else:
            list_of_stuff.append(left)
    return list_of_stuff
        

def recursive_zip(left, right):
    if isinstance(left, list) and isinstance(right, list):
        left = convert_to_list(left)
        right = convert_to_list(right)
        print("converr", left, right)
        # both values are lists, so zip them recursively
        return [(l, r) for l, r in zip(left, right)]
    else:
        # one or both values are not lists, so return them as a tuple
        return (left, right)

def compare(left, right):
    print("start", left, right)
    if isinstance(left, int) and isinstance(right, int):
        print("int", left, right)
        # both values are integers, so compare them directly
        print((left, "<=", right) if left <= right else (left, ">", right))
        return left <= right
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) == 1 or len(right) == 1:
            if isinstance(left[0], int) and isinstance(right[0], int):
                result = compare(left[0], right[0])
                if result:
                    # left value is lower, so return True
                    return True
                elif result is False:
                    # right value is lower, so return False
                    return False
            else:
                compare(left[0], right[0])
        else:
            left = convert_to_list(left)
            right = convert_to_list(right)
            print("lists", left, right)
            print(list(zip(left, right)))
            # both values are lists, so compare them item by item
            for l, r in zip(left, right):
                print("zip", l, r)
                result = compare(l, r)
                if result:
                    # left value is lower, so return True
                    return True
                elif result is False:
                    # right value is lower, so return False
                    return False
            # all items were equal, so return False
            return True
    else:
        print("convert", left, right)
        # one value is an integer and the other is a list, so convert the integer to a list and try again
        if isinstance(left, int):
            left = [left]
        elif isinstance(right, int):
            right = [right]
        if len(left) > len(right):
            return False
        else:
            return compare(left, right)

input = [[1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]]
resultslist = []
for x in range(len(input[0]) if len(input[0]) > len(input[1]) else len(input[1])):
    resultslist.append(compare(input[0][x], input[1][x]))
    
print(resultslist)