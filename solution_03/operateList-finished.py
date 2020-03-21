'''
将如下的车名放到列表cars中['bmw', 'audi', 'toyota', 'subaru'], 分别运用列表的一些常用函数操作列表，并查看其输出。(insert, append, pop, sort, sorted, len)

'''
print("\n")
cars=['bwm','audi','toyota','subaru']
cars.insert(4,'Lexus')
print(cars)

cars.append('Tesla')
print(cars)

favorate_car=cars.pop()
print(favorate_car)

cars.sort(reverse=True)
print(cars)

print(len(cars))




