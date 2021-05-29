# List to String
    # 1a. !!Iteration. Remember str(integer)
    def listToString(s): 
        str1 = ""
        for ele in s: 
            str1 += ele
        return str1

    s = ['Geeks', 'for', 'Geeks']
    print(listToString(s)) 

    # 1b. using join(). Won't work if the list contains both string and integer as its element. Need to convert it to string while adding to string.
    def listToString(s):
        str1 = " " 
        return (str1.join(s))
    
    s = ['Geeks', 'for', 'Geeks']
    print(listToString(s)) 
    
    # or better:
    return "".join(newLst)

    # 1c. Using list comprehension
    s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    listToStr = ' '.join([str(elem) for elem in s])
    print(listToStr) 

    #1d. Use map() method for mapping str (for converting elements in list to string) with given iterator, the list.
    s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    # using list comprehension
    listToStr = ' '.join(map(str, s))
    print(listToStr)


# 2 String removal
str = "Engineering"
 
print ("Original string: " + str)
 
res_str = str.replace('e', '') 

# removes all occurrences of 'e' 
print ("The string after removal of character: " + res_str) 
   
# Removing 1st occurrence of e 
 
res_str = str.replace('e', '', 1) 
    
print ("The string after removal of character: " + res_str) 

If you want to remove the central character:

midlen = len(oldstr)//2
newstr = oldstr[:midlen] + oldstr[midlen+1:]