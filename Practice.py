# 1732. find highest altitude: completed

# gain = [-5,1,5,0,-7]

# def highest_altitude(arr):
#     altitude = 0
#     high_point = 0
#     for i in arr:
#         altitude = altitude + i
#         # print(altitude)
#         if altitude > high_point:
#             high_point = altitude
#             # print(high_point)
#     return (high_point)


# print(highest_altitude(gain))


# 1. two sum completed



# def twosum(nums, target):
#     index1 = -1
#     for num1 in nums:
#         index1= index1 + 1
#         index2 = 0
#         for num2 in nums[1:]:
#             index2=index2+1
#             if num1 + num2 == target and index1 != index2:
#                 return[index1,index2]

# print(twosum([2,7,11,15], 9))

# 9 palindrome number : completed
# def palindrome(int):
#     word= str(int)
#     reverse_word= word[::-1]
#     if word == reverse_word:
#         return True
#     else:
#         return False

# print(palindrome(121))