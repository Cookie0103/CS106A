
# def fix_capitalization(str):
#     punctuation = [".", "!", "?"]
#     index_list = [i for i, ch in enumerate(str) if ch in punctuation]
#     index_list = check_contine(index_list)
#     # print(index_list)
#     if index_list is []:
#         turn_captialize(str)
#     if len(index_list) == 1:
#         result = ""
#         temp = str[:index_list[0]].lower()
#         temp = turn_captialize(temp)
#         result += temp
#         temp = str[index_list[0]:].lower()
#         temp = turn_captialize(temp)
#         result += temp
#         return result
#     if len(index_list)>=2:
#         result = ""
#         temp = str[:index_list[0]].lower()
#         temp = turn_captialize(temp)
#         # print(temp)
#         result += temp
#         for i in range(len(index_list)-1):
#             temp = str[index_list[i]:index_list[i+1]]
#             temp = turn_captialize(temp)
#             # print(temp)
#             result += temp
#         temp = str[index_list[len(index_list)-1]:].lower()
#         temp = turn_captialize(temp)
#         print(temp)
#         result += temp
#         return result

# def turn_captialize(str):
#     result = ""
#     str = str.lower()
#     for i in range(len(str)):
#         if str[i].isalpha():
#             result = str[:i] + str[i].upper() + str[i+1:]
#             break
#     return result
            
# def check_contine(i_list):
#     if i_list is []:
#         return []
#     else:
#         for i in range(len(i_list)-1):
#             if i_list[i]+1 == i_list[i+1]:
#                 i_list[i] = i_list[i+1]
#         return sorted(list(set(i_list)))

def fix_capitalization(str):
    # 结果是result=''，设置状态机next_cap=True,按字符遍历
    result = ''
    next_cap = True
    for ch in str:
        if ch.isalpha():
            if next_cap:
                ch = ch.upper()
                next_cap = False
            else:
                ch = ch.lower()
        elif ch in [".", "?", "!"]:
                next_cap = True
        result += ch
    return result
    

print(fix_capitalization("*almost done!! * that's AwESoME?! yes, IT IS."))
print(fix_capitalization("STANFORD ROCKS!!"))