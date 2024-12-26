def count(numbers):
    total = 0
    for x in numbers:
        if x < 20:
            total += 1
            
    return total

numbers = [1, 5, 10, 15, 20, 25, 30]

result = count(numbers)

print(result)

nums = [1,35,12,24,31,51,70,100]

def count(listOfNumbers):
    total = 0
    x = 0
    while x < len(nums):
        if nums[x] < 20:
            total += 1
        x += 1
        
    return total

print(count(nums))