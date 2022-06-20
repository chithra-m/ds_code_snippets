from click import secho


words=['this','that','is','if','that','is','if','this','that']
words_dict = {i:words.count(i) for i in words}
print(words_dict)

# {'this': 2, 'is': 2, 'if': 2, 'that': 3}
second_way = {}
for item in words:
    second_way[item] = words.count(item)

print(second_way)

for items in second_way:
    print(items)

print(second_way.items())
#dict_items([('this', 2), ('that', 3), ('is', 2), ('if', 2)])
#tuple of list of tuples