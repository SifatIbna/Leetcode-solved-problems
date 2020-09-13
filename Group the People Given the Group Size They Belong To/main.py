def answer(groupSizes):
    buckets = {}
    return_list = []

    for i,val in enumerate(groupSizes):
        if val in buckets.keys():
            buckets[val].append(i)
        else:
            buckets.update({val:[i]})
        if len(buckets[val]) == val:
            return_list.append(buckets[val])
            buckets[val] = []
    return return_list


print(answer([1,2,3,40,1]))