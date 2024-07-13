lowercase= list('abcdefghijklmnopqrstuvwxyz')
uppercase= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

data=[12331, 6909, 15145, 9792, 12944, 3027, 12611, 13520, 2347, 9024, 2330, 1406, 8982, 13254, 2348, 8988, 11875, 7271, 2580, 10796, 9039, 10414, 7217, 12110, 9053, 12970, 2420, 10536, 10835, 13445, 15652, 7907]
result="Y"
for num in range(len(data)-1):
    found=False
    for n1 in range(128):
        for n2 in range(128):
            for n3 in range(128):
                if n1^n2*n2^n3==data[num]:
                    result+=chr(n2)
                    found=True
                    break
            if found:
                break
        if found:
            break

print(result)
            
