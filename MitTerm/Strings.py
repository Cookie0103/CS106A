# def change_name_style(str):
#     camel_case = ""
#     str = str.split("_")
#     for chars in str:
#         camel_case += chars.capitalize()
#     print(camel_case)
#     return camel_case
        
def change_name_style(str):
    # 设置captial_next_letter默认True，遍历str，如果是_就改成True，如果不是就检查是否为True，为True就.upper()否则lower()
    result = ""
    captial_next_letter = True
    for i in range(len(str)):
        if str[i] == "_":
            capital_next_letter = True
        else:
            if capital_next_letter:
                result += str[i].upper()
                capital_next_letter = False
            else:
                result += str[i].lower()


change_name_style('three_word_name')
change_name_style('Four____Underscores')
change_name_style('_start_')