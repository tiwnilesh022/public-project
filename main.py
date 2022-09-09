import csv
with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    li = list(reader)
    
    count1 = 0
    for i in range(1,len(li)):
        if li[i][3] == "INNER_CITY" and li[i][10] == "YES":
            count1 = count1 + 1

    count2 = 0
    for i in range(1,len(li)):
        if li[i][3] != "INNER_CITY" and li[i][10] == "YES":
            count2 = count2 + 1

    count3 = 0
    for i in range(1,len(li)):
        if float(li[i][4]) >=1000 and float(li[i][4]) <=10000 and li[i][10] == "YES":
            count3 = count3 + 1

    count4 = 0
    for i in range(1,len(li)):
        if li[i][4] != "YES" and li[i][10] == "NO":
            count4 = count4 + 1

    count5 = 0
    for i in range(1,len(li)):
        if li[i][6] != "NO" and li[i][10] == "YES":
            count5 = count5 + 1

    print(count1/150*100)
    print(count2/150*100)
    print(count3/150*100)
    print(count4/150*100)
    print(count5/150*100)