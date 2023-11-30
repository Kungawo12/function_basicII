# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
def reverse_num(list):
    left = 0
    right = len(list)-1
    while (left < right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list

list_name =reverse_num([1,2,3,4,5])

print(list_name)