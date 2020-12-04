# day 1 part 1:
def find_double_value(l, answer):
    sorted_list = sorted(l)
    highest_value = answer - sorted_list[0]
    trunc_list = [x for x in sorted_list if x <= highest_value]
    final = False
    count = 0
    print(f"starting index {count}")
    for lowest in trunc_list:
        for item in trunc_list[count+1:]:
            if lowest + item == 2020:
               print("{} * {} = {}".format(lowest, item, lowest*item))
               final = True
               break
            elif lowest + item < 2020:
                continue
            elif lowest + item > 2020:
                break
        count += 1
        print(f"On index {count}")
        if final:
            break


# day 1 part 2:
def find_triple_value(l, answer):
    sorted_list = sorted(l)
    highest_value = answer - (sorted_list[0] + sorted_list[1])
    trunc_list = [x for x in sorted_list if x <= highest_value]
    # we have to either triple loop or keep track of values in a tree
    # i'm lazy so triple loop
    # lowest value
    count = 0
    final = False
    print(f"starting index {count}")
    for lowest in trunc_list:
        # value after first value
        for mid in trunc_list[count+1:]:
            # and after that
            for item in trunc_list[count+2:]:
                composite = lowest + mid + item
                if composite == answer:
                  print("{} * {} * {} = {}".format(lowest, mid, item, lowest*mid*item))
                  final = True
                  break
                elif composite < answer:
                  continue
                elif composite > answer:
                   break
            if final:
                break
        count += 1
        print(f"On index {count}")
        if final:
            break