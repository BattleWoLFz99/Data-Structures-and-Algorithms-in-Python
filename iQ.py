    #IF OR ELIF ......

# 0. Always start with asking questions:


    # Edge cases
    # Maybe some comments
    # Code Quality
    # Bug Free
    # Logicality
    # perhaps ask: “Would you like me to add comments to this?
    # They might expect you to ask certain questions
    # What is the type of return

    # iBinarySearch.py line 15 is elif, then else
    # NEVER DECLARING A VARIABLE IN IF STATEMENT, or better:
    #     Global variables are always at the beginning

    # Incoming data type
    # What should we return if we could not find the solution

# n Sum(BinarySearch):
    # Is the array sorted?
    # Does the array contain duplicated numbers?
    # Can we return same answers since there are duplicates?
    # Multiple solutions?

# 在写代码之前， 你会把所有你知道的解全部说出来， solution 1: ....  Solution 2:
#  .... Solution 3: ....   然后说 Time / space complexity for each solution.  
# 然后你就会发现有的solution 是有trade off 的 有的时间快了 但是用了额外的空间等等，
#  你需要和面试官讨论 他想让你 implement 哪一种方法， 这样不但展示了你知道很多种不同
# 的解 然后 还显示出你会分析 trade off  （是一个很好的工程师）。 最后 他想让你写哪一
# 种你就写哪一种（不过通常是比较优化的解）， 他也会比较满意。
# https://www.1point3acres.com/bbs/thread-623957-1-1.html
# https://www.1point3acres.com/bbs/thread-435598-1-1.html
# https://www.1point3acres.com/bbs/thread-433722-1-1.html

# 要知道每个公司的节奏。
# 不过，大概率是倾向于直接上最优解。那种要先写暴力再写最优的表演式做法已经过时了。比如说
# FB，45分钟两道题，你根本不可能有时间去表现演技的，只能是提一句暴力解法，然后自己把自己
# 否定掉，装作恍然大悟，突然想到的那种把最优解的思路讲出来。假惺惺的问一下面试官，你觉得
# 这样OK吗，我觉得可以，我写这个吧。然后把最优解默出来，debug，走corner case，分析复杂度。
# 狗家一般都是一道题目,加上一些follow up,如果题目有难度的话,可以考虑从暴力解开始.当然那
# 种看过去就很傻的暴力解还是不要去写了,没有意义,只会暴露自己很low

#记住你面试的目的是为了向一个水平75分的人证明你的水平过了60分线，而不是证明你的水平有90分