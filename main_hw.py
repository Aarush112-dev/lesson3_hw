list = [64,5,42,24,8,10,51,1,82,91,73]

count = 0
def check(list):
    for i in range(len(list)):
        flag = False
        for j in range(i,len(list)):
            if list[i] > list[j]:
                flag = True
                list[i], list[j] = list[j], list[i]
    print(list)
    return flag


check(list)
            



        