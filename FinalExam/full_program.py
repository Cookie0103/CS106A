FILENAME = 'D:\项目\CS106A\FinalExam\data2.txt'

# def main():
#     num_list = []
#     with open(FILENAME, "r") as file:
#         for line in file:
#             num_list.append(int(line.strip()))
#     # print(num_list)
#     i = 0
#     result = []
#     temp = [num_list[0]]
#     for i in num_list[1:]:
#         if i == temp[-1]+1:
#             temp.append(i)
#         else:
#             if len(temp)>1:
#                 result.append(temp)
#             temp = [i]
#             # print(temp)
#     if len(temp)>1:
#         result.append(temp)

#     # print(result)
#     max_len = len(result[0])
#     for x in result:
#         if len(x) > max_len:
#             max_len = len(x)
#     if max_len>0:
#         print(f"Longest chain: {max_len}")
#     else:
#         print("No chains found")
        
def main():
    # 记录prior_value=-1，max_chain和current_chain
    # 遍历line，保存value。看value是不是prior_value+1，如果是curr就+1，如果不是要看curr+1是不是比max_chain长，不是就回到原点。注意最后一个边界条件
    prior_value = -1
    max_chain = 0
    current_chain = 0
    with open(FILENAME) as file:
        for line in file:
            line = line.strip()
            value = int(line)
            if value == (prior_value+1):
                current_chain += 1
            else:
                if current_chain > 0 and current_chain+1 > max_chain:
                    max_chain = current_chain+1
                current_chain = 0
            prior_value = value
    if current_chain > 0 and current_chain+1 > max_chain:
        max_chain = current_chain+1
    
    if max_chain>0:
        print(f"Longest chain: {max_chain}")
    else:
        print("No chains found")
        
if __name__ == '__main__':
    main()