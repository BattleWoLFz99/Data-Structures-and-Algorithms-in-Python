# Pre-rep: el213 字符串压缩
# Solution 1:
# Wasted too much time on chars[:] holy...
# Be aware that chars is a list!! You will get ['A','B','12'] while ['A','B','1','2'] is expected
# Solution? Dont mod blablabla so stupid, just use a string then chars[:] = list(compressed) lol
# Obiviously not the best solution()
class Solution:
    def compress(self, chars: List[str]) -> int:
        # write your code here
        idx1,idx2 = 0,0
        compressed = ""
        while idx1 < len(chars):
            count = 0
            while idx2 < len(chars) and chars[idx1] == chars[idx2]:
                idx2 += 1
                count += 1
            if count > 1:
                compressed += chars[idx1]
                compressed += str(count)
                idx1 = idx2
            else:
                compressed += chars[idx1]
                idx1 = idx2
        chars[:] = list(compressed)
        return len(chars)

# Solution 2 O(1) space:
class Solution:
    def compress(self, chars: List[str]) -> int:
        # write your code here
        idx1,idx2 = 0,0
        #  compressed = ""
        idx3 = 0
        while idx1 < len(chars):
            count = 0
            while idx2 < len(chars) and chars[idx1] == chars[idx2]:
                idx2 += 1
                count += 1
            if count > 1:
                #  compressed += chars[idx1]
                chars[idx3] = chars[idx1]
                idx3 += 1
                #  compressed += str(count)
               #chars[idx3] = str(count) ?
               #idx3 += 1 ?
                # But what if b repeats 11? So:
                for c in str(count):
                    chars[idx3] = c
                    idx3 += 1
                idx1 = idx2
            else:
                #  compressed += chars[idx1]
                chars[idx3] = chars[idx1]
                idx3 += 1
                idx1 = idx2
        
        return idx3

# Discuss solution:
# for chars = aabcccdddd you get a2bc3d4ddd, I assume there is something like chars[0:walker] in the black box
class Solution:
    def compress(self, chars: List[str]) -> int:
        walker, runner = 0, 0
        while runner < len(chars):
		
            chars[walker] = chars[runner]
            count = 1

            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1
			
            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            
			runner += 1
            walker += 1
        
        return walker
