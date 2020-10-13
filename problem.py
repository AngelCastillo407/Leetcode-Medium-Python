print

arr = [4, 3, 1, 1, 3, 3, 2]
k = 3

print "Given an array of", arr

solution = 0
distinctNums = 0
newK = k

arr.sort()

countList = []
currentCount = 0
currentNum = arr[0]

y = len(arr)

for x in range(0, y):

    if arr[x] != currentNum and x == y - 1:
        countList.append(currentCount)
        countList.append(1)

    elif arr[x] != currentNum:
        countList.append(currentCount)
        currentCount = 1
        currentNum = arr[x]

    elif arr[x] == currentNum and x == y - 1:
        currentCount += 1
        countList.append(currentCount)

    elif arr[x] == currentNum:
        currentCount += 1

countList.sort()
distinctNums = len(countList)

for x in range(0, distinctNums):

    if newK < 0:
        break

    elif newK - countList[x] >= 0:
        solution += 1
        newK -= countList[x]


print "the least number of unique integers after removing exactly", k, "elements is", distinctNums - solution