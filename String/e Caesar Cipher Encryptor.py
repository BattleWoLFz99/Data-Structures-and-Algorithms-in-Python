'''
Sample Input = "xyz"
Key = 2

Sample Output: zab

Bacause x+2 = z, y+2-26 = a
'''

# ord ASCII chr: A-Z: 065-090; a-z: 097-122; 0-9:048-057

def caesarCipherEncryptor(string, key):
    newString = []
    #Note that key can be like 100
    newKey = key % 26
    for s in string:
        ascii = ord(s) + newKey
        if ascii > 122:
            ascii = ascii - 26
        newString.append(chr(ascii))
    return newString #However, it returns a list

print(caesarCipherEncryptor("wxyz", 2))

# Return a string
def caesarCipherEncryptor(string, key):
    # Write your code here.
    if not string:
		return 
	
	newLst = []
	newkey = key % 26
	
	for i in string:
		ascii = ord(i) + newkey
		if ascii > 122:
			ascii -=26
		newLst.append(chr(ascii))
		
	return "".join(newLst)