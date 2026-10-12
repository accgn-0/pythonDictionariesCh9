'''

bag = dict()
bag['ballpen'] = 2
bag['ballpen'] = bag['ballpen'] + 1

count = dict()
names = ['john', 'lia', 'rom',]
for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[names]=count[name]+1
print(count)

#easy command in python 'get' method
## x = count.get(name, 0)

'''

counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()
print('Words: ', words)
print('Counting...')
for word in words:
    counts[word]= counts.get(word, 0)+1
print('Counts', counts)

fhand = open('text.txt', 'r')
