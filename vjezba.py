import nltk

with open('read.txt', 'r') as file:
    #file.read() ovako ucita cijeli file u buffer
    korpus = file.read().split()
    novi = nltk.Text(korpus)
    # print(korpus)

file.closed
print(f"Korpus: {len(korpus)}")
print(f"Novi: {len(novi)}")
print()
print(f"Korpus: {len(set(korpus))}")
print(f"Novi: {len(set(novi))}")
print()
