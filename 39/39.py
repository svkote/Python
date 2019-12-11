things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'f'
print(things[1])
print(things)

del things[1]
print(things[1])
print(things)

stuff = {'name': 'Lex', 'age': 38, 'wight': 6*12+2}
print(stuff['name'])
stuff['city'] = 'Moscow'
stuff[1] = 'Yes'
print(stuff)
del stuff[1]
print(stuff)

