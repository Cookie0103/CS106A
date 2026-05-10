# Strings
def remove_doubled_letters(str):
    removed_str = "" + str[0]
    for ch in str[1:]:
        if removed_str[-1] != ch:
            removed_str += ch
    return removed_str


print(remove_doubled_letters('tresidder'))
print(remove_doubled_letters('bookkeeper'))