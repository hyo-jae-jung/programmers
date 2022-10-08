dartResult = '1S2D*3T'

num_list = []
num = 0
for i in dartResult:
    try:
        num+=int(i)
    except:
        num_list.append(num)
        num=0

print(num_list)
