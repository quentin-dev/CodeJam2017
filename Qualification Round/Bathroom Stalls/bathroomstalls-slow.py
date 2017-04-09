# WARNING : THIS CODE TAKES EXCESSIVELY LONG AND DOES NOT WORK PROPERLY

def init_stalls(n):
    stalls = []
    for i in range (n+2):
        if i == 0:
            stalls.append((0,n,True))
        elif i == n+1:
            stalls.append((n,0,True))
        else:
            stalls.append((i-1, n-i, False))
    return (stalls)

def best_stall(arr):
    maxmin_found = -1
    openS = []
    for i in arr:
        if(min(i[0],i[1]) >= maxmin_found and not i[2]):
            #print(not i[2])
            if (maxmin_found == min(i[0],i[1])):
                #print(arr.index(i))
                openS.append(arr.index(i))
            else:
                openS = [arr.index(i)]
            maxmin_found = min(i[0],i[1])
    if (len(openS) > 1):
        maxmax_found = -1
        leftS = []
        for j in openS:
            #print(j)
            if (max(arr[j][1],arr[j][0]) >= maxmax_found):
                if (maxmax_found == max(arr[j][1],arr[j][0])):
                    leftS.append(j)
                else:
                    leftS = [j]
                maxmax_found = max(arr[j][1],arr[j][0])
        if (len(leftS) > 1):
            return(min(leftS))
        else:
            return(leftS[0])
    else:
        return(openS[0])
    #return(maxmin_found)

def update_stalls(arr, index):
    #print(index)
    for i in range (0, len(arr)):
        if (i < index):
            if (index-i-1 < 0):
                rep = 0
            else:
                rep = index-i-1
            arr[i] = (arr[i][0], rep,arr[i][2])
        elif (i > index):
            if (arr[i][0] - index < 0):
                rep = 0
            else :
                rep = arr[i][0] - index
            arr[i] = (rep, arr[i][1], arr[i][2])
        else:
            arr[i] = (arr[i][0], arr[i][1], True)
    return(arr)

infile = open("C-small-1-attempt0.in",'r')
out = open("out-slow.txt", 'w')
num_prob = int(infile.readline())
i = 0
for line in infile:
    i += 1
    numStalls, people = [int(s) for s in line.split(" ")]
    room = init_stalls(numStalls)
    #print(people)
    for p in range (people):
        best = best_stall(room)
        room = update_stalls(room, best)
    #end = best_stall(room)
    #print(room)
    val = "Case #{}: {} {}\n".format(i, max(room[best][0], room[best][1]), min(room[best][0], room[best][1]))
    #print(room[best])
    #print(val)
    out.write(val)
infile.close()
out.close()