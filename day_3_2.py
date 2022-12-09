priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_sum = 0

filename = 'day3_input.txt'
with open(filename) as f:
    content = f.read().splitlines()

#print(content)

def grouping(start, content):
    group = []
    group.append(content[start])
    group.append(content[start+1])
    group.append(content[start+2])
    return group

# print(grouping(0, content))
priority_list = []
for i in range(0, len(content), 3):
    for group in grouping(i, content):
        print(group[i])
        #print(grouping(i, content), grouping(i, content)[1], grouping(i, content)[2])
        if group[i] in grouping(i, content)[1] and group[i] in grouping(i, content)[2]:
            #print(group[i])
            pass

"""for line in content:
    priority_list = []

    for i in range(len(line)):
        pass"""
    #priority_sum += priority_list[0]
    #print(priority_sum)
