# Duplicates Not Allowed

hashing = set()
hashing = set(lst)

# return the only ele in set
# return hashing.pop()

# way slower, if don't want to remove:
e = next(iter(hashing))
# or
>>> S = {1}
>>> min(S)
1
>>> S
set([1])
>>> max(S)
1
>>> S
set([1])


>>> x = set('spam')
>>> y = set(['h','a','m'])
>>> x, y
(set(['a', 'p', 's', 'm']), set(['a', 'h', 'm']))
 
再来些小应用。
 
>>> x & y # 交集
set(['a', 'm'])
 
>>> x | y # 并集
set(['a', 'p', 's', 'h', 'm'])
 
>>> x - y # 差集
set(['p', 's'])


基本操作：
t.add('x')            # 添加一项
s.update([10,37,42])  # 在s中添加多项

使用remove()可以删除一项：
t.remove('H')
 
len(s)
set 的长度
 
x in s
测试 x 是否是 s 的成员
 
x not in s
测试 x 是否不是 s 的成员
 
s.issubset(t)
s <= t
测试是否 s 中的每一个元素都在 t 中
 
s.issuperset(t)
s >= t
测试是否 t 中的每一个元素都在 s 中
 
s.union(t)
s | t
返回一个新的 set 包含 s 和 t 中的每一个元素
 
s.intersection(t)
s & t
返回一个新的 set 包含 s 和 t 中的公共元素
 
s.difference(t)
s - t
返回一个新的 set 包含 s 中有但是 t 中没有的元素
 
s.symmetric_difference(t)
s ^ t
返回一个新的 set 包含 s 和 t 中不重复的元素
 
s.copy()
返回 set “s”的一个浅复制


请注意：union(), intersection(), difference() 和 symmetric_difference() 的非运算
符（non-operator，就是形如 s.union()这样的）版本将会接受任何 iterable 作为参数。相反
，它们的运算符版本（operator based counterparts）要求参数必须是 sets。这样可以避免潜
在的错误，如：为了更可读而使用 set('abc') & 'cbs' 来替代 set('abc').intersection('cbs')。
从 2.3.1 版本中做的更改：以前所有参数都必须是 sets。
 
另外，Set 和 ImmutableSet 两者都支持 set 与 set 之间的比较。两个 sets 在也只有在这种
情况下是相等的：每一个 set 中的元素都是另一个中的元素（二者互为subset）。一个 set 比另
一个 set 小，只有在第一个 set 是第二个 set 的 subset 时（是一个 subset，但是并不相等
）。一个 set 比另一个 set 打，只有在第一个 set 是第二个 set 的 superset 时（是一个
superset，但是并不相等）。
 
子 set 和相等比较并不产生完整的排序功能。例如：任意两个 sets 都不相等也不互为子 set，
因此以下的运算都会返回 False：a<b, a==b, 或者a>b。因此，sets 不提供 __cmp__ 方法。
 
因为 sets 只定义了部分排序功能（subset 关系），list.sort() 方法的输出对于 sets 的列表
没有定义。
 
 
运算符
   运算结果
 
hash(s)
   返回 s 的 hash 值
 
 
下面这个表列出了对于 Set 可用二对于 ImmutableSet 不可用的运算：
 
运算符（voperator）
等价于
运算结果
 
s.update(t)
s |= t
返回增加了 set “t”中元素后的 set “s”
 
s.intersection_update(t)
s &= t
返回只保留含有 set “t”中元素的 set “s”
 
s.difference_update(t)
s -= t
返回删除了 set “t”中含有的元素后的 set “s”
 
s.symmetric_difference_update(t)
s ^= t
返回含有 set “t”或者 set “s”中有而不是两者都有的元素的 set “s”
 
s.add(x)
 
向 set “s”中增加元素 x
 
s.remove(x)
 
从 set “s”中删除元素 x, 如果不存在则引发 KeyError
 
s.discard(x)
 
如果在 set “s”中存在元素 x, 则删除
 
s.pop()
 
删除并且返回 set “s”中的一个不确定的元素, 如果为空则引发 KeyError
 
s.clear()
 
删除 set “s”中的所有元素
 
 
请注意：非运算符版本的 update(), intersection_update(), difference_update()和symmetric_difference_update()将会接受任意 iterable 作为参数。从 2.3.1 版本做的更改：以前所有参数都必须是 sets。
 
还请注意：这个模块还包含一个 union_update() 方法，它是 update() 方法的一个别名。包含这个方法是为了向后兼容。程序员们应该多使用 update() 方法，因为这个方法也被内置的 set() 和 frozenset() 类型支持。
