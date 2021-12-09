# 1
x = int(input("Введите число: "))

def binary_search(sorted_lst, item):
    low = 0
    high = len(sorted_lst) - 1
    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if sorted_lst[mid] == item:
            found = True
        else:
            if item <= sorted_lst[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return ("Такого числа нет" if found == False else "Число " + str(x) + " в списке присутсвует")

lst = [97, 63, 14, 42, 39, 6, 15, 71, 34, 10]
sorted_lst = sorted(lst)
print(sorted_lst)

print(binary_search(sorted_lst, x))

# 2

nums = [-2, 3, 8, -11, -4, 6]


def count_nums(nums):
    count = 0
    for i in nums:
        if i < 0:
            count += 1
    return count


print(count_nums(nums))