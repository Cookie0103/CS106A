
# def interleave_lists(list1, list2):
#     # if list1 is [] or list2 is []:
#     #     return list1 + list2
#     # if list1 is [] and list2 is []:
#     #     return []
#     result = []
#     shortest = min(len(list1), len(list2))
#     for i in range(shortest):
#         result.append(list1[i])
#         result.append(list2[i])
#     result = result + list1[shortest:] + list2[shortest:]
#     return result

def interleave_lists(list1, list2):
    # 返回result， 计算min_length，比较两个列表的大小用remainder去做extend
    result = []
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        result.append(list1[i])
        result.append(list2[i])
    if len(list1)<len(list2):
        remainder = list2[min_length:]
    else:
        remainder = list1[min_length:]
    result.extend(remainder)
    return result

first = [1, 2, 3, 4, 5, 6, 7] 
second = [10, 20, 30, 40]   
third = [100] 
            
print(interleave_lists(third, first))