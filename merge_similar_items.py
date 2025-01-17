items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]


def merge_items(items1, items2):
    res = items1 if len(items1) > len(items2) else items2
    min_it = items2 if len(items2) < len(items1) else items1

    for i in range(len(res)):
        for j in range(len(min_it)):
            if res[i][0] == min_it[j][0]:
                res[i][1] += min_it[j][1]
    for i in range(len(min_it)):
        if min_it[i][0] not in [item[0] for item in res]:
            res.append(min_it[i])


    res.sort(key=lambda x: (x[0]))
    return res


def merge_items_2(items1, items2):
    m1 = {value: weight for value, weight in items1}
    ret = []
    for item in items2:
        value, weight = item
        if not m1.get(value):
            m1[value] = weight
        else:
            m1[value] += weight
    for value,weight in m1.items():
        ret.append([value,weight])
    ret.sort()
    return ret



item2 = [[5,1],[4,2],[3,3],[2,4],[1,5]]
item4 = [[7,1],[6,2],[5,3],[4,4]]


print(merge_items_2(item2, item4))