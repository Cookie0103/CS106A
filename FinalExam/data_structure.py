
# def add_bignums(bignum1, bignum2):
#     result = []
#     longer = max(len(bignum1), len(bignum2))
#     temp = 0
#     for i in range(longer):
#         sum_num = temp + get(bignum1, i) + get(bignum2, i)
#         if sum_num < 10:
#             result.append(sum_num)
#             temp = 0
#         else:
#             if i == longer-1:
#                 result.append(sum_num % 10)
#                 result.append(1)
#             else:
#                 result.append(sum_num % 10)
#                 temp = 1
#     return result

# def get(lst, i):
#     return lst[i] if i>=0 and i<len(lst) else 0

def add_bignums(bignum1, bignum2):
    # result返回结果，carry计算十位默认是0，遍历max_size,把位加起来。看sum是否>=10，result添加的是sum，如果最后一位是要进的话最后result再append
    result = []
    carry = 0
    max_size = max(len(bignum1), len(bignum2))
    for i in range(max_size):
        sum = carry + safe_get_digit(bignum1, i) + safe_get_digit(bignum2, i)
        if sum >= 10:
            carry = 1
            sum = sum - 10
        else:
            carry = 0
        result.append(sum)
    if carry == 1:
        result.append(carry)
    return result
    
def safe_get_digit(bignum, index):
    if index >= len(bignum):
        return 0
    else:
        return bignum[index]


print(add_bignums([4, 6, 5], [7, 6, 8]))