array = [10,20,30,40,50,60,70,80]
res = array[0]
for i in range(0, len(array)):
    if (array[i] > res):
        res = array[i]

print("The largest no. is:" + str(res))