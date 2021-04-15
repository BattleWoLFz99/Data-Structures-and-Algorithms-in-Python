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

    # 1c. Using list comprehension
    s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    listToStr = ' '.join([str(elem) for elem in s])
    print(listToStr) 

    #1d. Use map() method for mapping str (for converting elements in list to string) with given iterator, the list.
    s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
    # using list comprehension
    listToStr = ' '.join(map(str, s))
    print(listToStr)