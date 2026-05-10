# def contains_loop(filename):
#     friend_dict = {}
#     with open(filename) as file:
#         for line in file:
#             parts = line.split()
#             friend_dict[parts[0]] = parts[1]
#     best_friend = []
#     for key in friend_dict:
#         if search(key, friend_dict):
#             return True
#     return False
#     #     best_friend.append(temp)
#     # if any(best_friend):
#     #     return True
#     # return False

# def search(name, friend_dict):
#     met_dict = [name]
#     curr = name
#     while curr in friend_dict:
#         curr = friend_dict[curr]
#         if curr not in met_dict:
#             met_dict.append(curr)
#         else:
#             return True
#     return False

def contains_loop(filename):
    # 创建一个bf_dict, 读取文件（line, names）
    # for循环遍历name，path列表保存关系，while循环看name是不是在key里面，paht添加，name遍历，如果name在path里返回True
    bf_dict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            names = line.split()
            bf_dict[names[0]] = names[1]
    
    for name in bf_dict.keys():
        path = []
        while name in bf_dict:
            path.append(name)
            name = bf_dict[name]
            if name in path:
                return True
    return False

print(contains_loop("D:\项目\CS106A\FinalExam\data.txt"))