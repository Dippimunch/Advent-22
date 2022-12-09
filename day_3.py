priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_sum = 0


filename = 'day3_input.txt'
with open(filename) as f:
    content = f.read().splitlines()

for line in content:
    priority_list = []
    first_half = line[:(int(len(line)/2))]
    second_half = line[-(int(len(line)/2)):]
    #print(line, '\n', first_half, second_half, '\n\n')
    print(first_half, second_half)

    for i in range(len(first_half)):
        if first_half[i] in second_half:
            priority_list.append(priority.index(first_half[i]) + 1)
            print('TRUE')
            print(first_half[i], int(priority.index(first_half[i])) + 1)
            #priority_sum += priority_list[0]
    
    priority_sum += priority_list[0]
    print(priority_sum)

    

    #print('priorty_list: ', priority_list)
    #priority_sum += priority_list[0]
