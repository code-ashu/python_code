#### buble Sort program 
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
        
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example usage
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Sorted array using Bubble Sort:", arr)


# ## sort list using sorted method  ##
# first_lst = [19, 21, 12, 15, 18, 2, -5, 10]
# sorted_lst = sorted(first_lst)
# print(sorted_lst[-2])


# # wap find second max element ##
# def secmax(k, no):
#     for i in range(0,len(k)):
#         for j in range(i+1, len(k)):
#             if k[i] > k[j]:
#                 k[i],k[j] = k[j],k[i]

#     if no <= len(k):
#         print(f"the {no}th largest element is: {k[-no]}")
#     else:
#         print("Invalid input the list doen not have many elements")

# lst = [19, 21, 12, 15, 18, 2, -5, 10]
# number =int(input("Enter the position of 2nd largest element"))
# secmax(lst, number)


# ##  wap create list of duplicate element and create lst of remove duplicate element ##
# def duple_ele(lst):
#     dupl_lst = []
#     remove_dupl = []
#     for i in lst:
#         if i not in remove_dupl:
#             remove_dupl.append(i)
#         else:
#             dupl_lst.append(i)
#     return dupl_lst, remove_dupl


# first_lst = [19, 21, 12, 15, 18, 2, -5, 10, 3, 3, 3, 21, 18]
# result = duple_ele(first_lst)
# print(f" Duplicates from given list {result[0]} and removed duplicated elements list {result[1]}.")


# ## ###  delete elements from list  ###
# first_lst = [19, 21, 12, 15, 18, 2, -5, 10, 3, 3, 3, 21, 18]
# first_lst.pop()
# print(first_lst)
# first_lst.remove(-5)
# print(first_lst)
# print(tuple(first_lst))

# ## ### find of occur_chr using dict comprehension ###
# roles = 'ADDFGGGGGGDDDDDDDEEEEE'
# occur_chr = {ele: roles.count(ele) for ele in roles}
# print(occur_chr)

# roles = 'ADDFGGGGGGDDDDDDDEEEEE'
# occur_chr = {}
# for i in roles:
#     occur_chr[i] = occur_chr.get(i, 0) + 1
# print(occur_chr)

# designation = 'Python Automation Test Engineer'
# rev_str = designation[::-1]
# print(rev_str)

# designation = 'Python Automation Test Engineer'
# rev_str = ''.join((reversed(designation)))
# print(rev_str)


# designation = 'Python Automation Test Engineer'
# rev_str = ''
# for i in designation:
#     rev_str = i + rev_str

# print(rev_str)

# ## ## using the split method and that will generate list   ###
# designation = 'Python Automation Test Engineer'
# split_lst = designation.split()
# print(split_lst[::-1])


# # ## reverse str using while loop   ##
# designation = 'Python Automation Test Engineer'
# split_lst = designation.split()
# rev_lst = []
# i = len(split_lst)-1
# while i >= 0:
#     rev_lst.append(split_lst[i])
#     i = i-1
# print(rev_lst)

# #  ##  rverse string using split and for loop  ##
# designation = 'Python Automation Test Engineer'
# split_lst = designation.split()
# # print(' '.join(reversed(split_lst)))
# # print(' '.join(split_lst[::-1]))
# rev_sent = ' '
# for i in split_lst:
#     rev_sent = i + ' ' + rev_sent
# print(rev_sent)


# # ## wap create generator function by taking 1 to 5 number & generate square of that number by using decorator
# def square_generator(func):
#     def wrapper():
#         gen = func()
#         return (x**2 for x in gen)
#     return wrapper
  
# @square_generator
# def number_generator():
#     for i in range(1, 6):
#         yield i

# # Using the decorated generator
# gen = number_generator()
# for square in gen:
#     print(square)

# # ## wap for Decorator function    ##
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()  # Call the original function
#         print("Something is happening after the function is called.")
#     return wrapper

# # Applying the decorator using @decorator syntax
# @my_decorator
# def say_hello():
#     print("Hello!")

# # Calling the decorated function
# say_hello()


# ### wap create gen fun by taking 1 to 5 number & on that we add 5 number using decorator ##
# def decor(func):
#     def wrapper():
#         a =func()
#         print(a)
#         return (x+5 for x in a)
#     return wrapper
# @decor
# def num():
#     for i in range(0,5):
#         yield i
# k = num()
# print(k)
# for add in k:
#     print(add)


### ##  1st Approch write a program for Find the median
# numbers =[10,17,18,15]
# numbers.sort()
# length =len(numbers)
# middle = length //2 
# print(middle)
# if length % 2 == 0:
#     median = (numbers[middle-1] +numbers[middle]) / 2
# else:
#     median = numbers[middle]
# print("median is:", median)


# ## 2nd Approch write a program for Find the median ##
# def find_median(lst):
#     n = len(lst)
#     middle = n // 2

#     for i in range(0, n - 1):
#         for j in range(n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]

#     if n % 2 == 0:
#         median = (lst[middle - 1] + lst[middle]) / 2
#     else:
#         median = lst[middle]
#     return median


# list1 = [10, 17]
# list2 = [18, 15]
# concatenated_list = list1 + list2
# median = find_median(concatenated_list)

# print("Concatenated list:", concatenated_list)
# print("Median of the list:", median) 


# # ##  write a program for flatten dictionary  ##
# def flatten_dict(d, parent_key='', sep='_'):
#     items = {}
#     for k, v in d.items():
#         new_key = parent_key + sep + k if parent_key else k
#         if isinstance(v, dict):
#             items.update(flatten_dict(v, new_key, sep=sep))
#         else:
#             items[new_key] = v
#     return items

# nested_dict = {
#     'l': 1,
#     'm': {
#         's': 2,
#         'n': {
#             'f': 3
#         }
#     }
# }
# flattened_dict = flatten_dict(nested_dict)
# print(flattened_dict)

### wap of anagram string ###
# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase for comparison
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if the lengths are equal
#     if len(str1) != len(str2):
#         return False

#     # Count occurrences of characters in both strings
#     char_count = {}

#     for char in str1:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     for char in str2:
#         if char in char_count:
#             char_count[char] -= 1
#         else:
#             return False

#     # Check if all counts are zero
#     for count in char_count.values():
#         if count != 0:
#             return False

#     return True

# # Example usage
# string1 = "listen"
# string2 = "silent"
# if are_anagrams(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

#### 2nd approch of anagram string ####
# def is_anagram(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if the length of both strings are equal
#     if len(str1) != len(str2):
#         return False

#     # Sort the characters in both strings and compare
#     return sorted(str1) == sorted(str2)

# # Test the function with the given strings
# str1 = "icemanun"
# str2 = "cienmanu"
# if is_anagram(str1, str2):
#     print(f"'{str1}' and '{str2}' are anagrams.")
# else:
#     print(f"'{str1}' and '{str2}' are not anagrams.")

### check the string is palindrom or not ###
# def is_palindrome(s):
#     return s == s[::-1]

# str1 = "racecar"
# if is_palindrome(str1):
#     print("The String is Palindrom")
# else:
#     print("the string is not palindrom")


#### find substring from that "ababacb" string  ######
### o/p abab,ababa,bac,abacb,baba,bacb,babacb,babac,abac,bab,acb,aba,ababac,ababacb ##
# def generate_substrings(s):
#     length = len(s)
#     substrings = set()

#     for i in range(length):
#         for j in range(i + 1, length + 1):
#             #The substring starts at index i and ends at index j - 1.
#             substring = s[i:j]  
#             print(substring)
#             if len(substring) >= 3:
#                 substrings.add(substring)
#     return substrings

# str_input = "ababacb"
# unique_substrings = generate_substrings(str_input)
# print(','.join(unique_substrings))


#### wap for finding missing numbers ####
# def find_missing_numbers(nums):
#     expected_nums = list(range(nums[0], nums[-1] + 1))
#     print(expected_nums)
#     missing_nums = [num for num in expected_nums if num not in nums]
#     return missing_nums

# nums = [1,2,3,5,4,7,9,13]
# missing_nums = find_missing_numbers(nums)
# print("Missing numbers:",missing_nums)


### write a program to add pair output(1,14) sum should be 15, &(12,3) sum 15
## o/p [(1, 14), (12, 3)]
# list =[ 1,14,2,5,6,8,5,12,3,8]
# l=len(list)
# k=15
# tup=()
# m =[]
# for i in range(l):
#     for j in range(i+1,l):
#         if list[i] + list[j] ==k:
#             tup=(list[i],list[j])
#             m.append(tup)
# print(m)


##### anagram list ###
ana = ['ate', 'eat', 'tea', 'bat', 'tab', 'abt']
anagram_dict = {}

for word in ana:
    sored_word = ''.join(sorted(word))
    print(sored_word )
    if sored_word not in anagram_dict:
        anagram_dict[sored_word] = [word]
    else:
        anagram_dict[sored_word].append(word)

a = list(anagram_dict.values())
print(a)

#### wap count of vowels from string ####
#### o/p  {'a': 3, 'e': 4, 'i': 4, 'o': 3, 'u': 1} ###
def check_vow(string, vowels):
    string =string.casefold()
    print(string)
    count ={}.fromkeys(vowels,0)
    print(count)
    for character in string:
        if character in count:
            count[character] +=1
    return count
vowels = "aeiou"
string ="Hi, I love eating ice creamand junk food"
print(check_vow(string, vowels))


#### wap find duplicate word in string  ####
#### o/p ['easy']  1st Approch 
def find_duplicates(sentence):
    words = sentence.split()
    duplicates = []
    for word in words:
        if words.count(word) > 1 and word not in duplicates:
            duplicates.append(word)
    return duplicates

sentence = "python is very easy easy"
duplicate_words = find_duplicates(sentence)
print("Duplicate words:", duplicate_words)
