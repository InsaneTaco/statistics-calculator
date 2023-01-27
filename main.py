import statistics

while True:
    count = 0
    datalist = []
    madDifference = []
    
    # user enters data set separated by space
    print('Enter data set of numbers separated by space. eg: "1 2 3"')
    data = input()
    datalist = list(map(float, data.split(" ")))
    datalist.sort()
    
    print(f"""
{datalist}""")

    # mean
    mean = statistics.mean(datalist)
    print(f"mean: {mean}")

    # mad
    for item in datalist:
        madDifference.append(abs(item - mean))
        count += 1

    print(f"mad: {statistics.mean(madDifference)}")
    
    # median
    print(f"median: {statistics.median(datalist)}")

    # mode
    print(f"mode: {statistics.mode(datalist)}")

    print(f"instances: {count}")

    # range
    print(f"""range: {max(datalist) - min(datalist)}
    """)