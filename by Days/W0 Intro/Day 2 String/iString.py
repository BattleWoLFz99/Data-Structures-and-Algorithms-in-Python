# el241, "-123" to -123:
# return int(str) 可以处理负号，正号也能处理的

# el146, Input: str = "abC12", Output: "ABC12"
# return str.upper()  无视integer

# 说是这么说，还是照常写吧233

# 1. List to String
#   return "".join(newLst)

    # 1c. Using list comprehension
    s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    listToStr = ' '.join([str(elem) for elem in s])
    print(listToStr) 

    #1d. Use map() method for mapping str (for converting elements in list to string) with given iterator, the list.
    s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    # using list comprehension
    listToStr = ' '.join(map(str, s))
    print(listToStr)

# 2. String to List:
# string.split(separator, maxsplit) 
# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
# ['apple', 'banana', 'cherry', 'orange']

# string.replace(oldvalue, newvalue, count)
# oldvalue	Required. The string to search for
# newvalue	Required. The string to replace the old value with
# count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
var_str = 'Zhuge_Dan#Susan_Molina#Zhuge_Dan#Jennifer_Lee#Jerry_Davis#'
var_list = var_str.replace("_"," ").split("#")
# ['Zhuge Dan', 'Susan Molina', 'Zhuge Dan', 'Jennifer Lee', 'Jerry Davis']


# 3. String removal
    # Remove First Character from a String: 
    strObj = strObj[1 : : ]
    # Remove Last Character from a String:
    strObj = strObj[:-1:]
    # Remove multiple characters from a string in given index range
    strObj = strObj[0: start:] + strObj[stop + 1::]


strObj = "This is a sample string"
str = "Engineering"
print ("Original string: " + str)
res_str = str.replace('e', '') 

# removes all occurrences of 'e' 
print ("The string after removal of character: " + res_str) 
   
# Removing 1st occurrence of e 
 
res_str = str.replace('e', '', 1) 
    
print ("The string after removal of character: " + res_str) 

# If you want to remove the central character:

midlen = len(oldstr)//2
newstr = oldstr[:midlen] + oldstr[midlen+1:]

# 4. The .isalnum() returns:
#       True if all characters in the string are alphanumeric
#       False if at least one character is not alphanumeric
# .isdigit()  .isalpha()  .lower()  .upper()
#       .isalnum() == char.isditgit() or char.isalpha()

# 5. Consider two pointers. O(n) space is usually a bad solution

# 6. string = "I want you"
# lst = list(string)
# print(lst)
# ['I', ' ', 'w', 'a', 'n', 't', ' ', 'y', 'o', 'u']

# lst = string.split()
# print(lst)
# ['I', 'want', 'you']