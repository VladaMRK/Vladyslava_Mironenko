"""
Upper and Lower
"""
# Provide your solution here


def count_upper_lower(string: str):
    count_upper = 0
    count_lower = 0
    for letter in string:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1

    print(f"No. of Upper case characters: {count_upper}")
    print(f"No. of Lower case characters: {count_lower}")





"""
Check 33
"""
# Provide your solution here


def has_33(list_of_integers: list) -> bool:
    list_of_integers2 = str(list_of_integers)
    return("3, 3" in list_of_integers2)









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")


print(count_upper_lower("Fi3"))
print(count_upper_lower("FiFig"))

print(has_33([1, 3, 5, 6, 7, 3, 8, 9]))
print(has_33([1, 3, 5, 6, 7, 3, 3, 3, 8, 9]))