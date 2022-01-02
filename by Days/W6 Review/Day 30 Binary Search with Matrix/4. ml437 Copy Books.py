# Better understanding
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0
            
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
                
        if self.get_least_people(pages, start) <= k:
            return start
            
        return end
        
    def get_least_people(self, pages, time_limit):
        count = 1
        time_cost = 0 
        for page in pages:
            if time_cost + page <= time_limit:
                time_cost += page
            else:
                count += 1
                time_cost = page
            
        return count



# Not sure since it increases logic complexity a little bit..
# 关键很容易写错的样子草先放着吧题刷少了是肯定的未来回顾
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if not pages:
            return 0
            
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
                
        if self.get_least_people(pages, start) <= k:
            return start
            
        return end
        
    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0 
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page
            
        return count + 1