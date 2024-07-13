lowercase= list('abcdefghijklmnopqrstuvwxyz')
uppercase= list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# This code tries to reverse the modified xor function used by the Riddler. It tries a brute-force approach, which turned out to work well for all letters except a few letters where there is a choice of 0 or 1, and which of the two to choose has to be checked. 
data=[12331, 6909, 15145, 9792, 12944, 3027, 12611, 13520, 2347, 9024, 2330, 1406, 8982, 13254, 2348, 8988, 11875, 7271, 2580, 10796, 9039, 10414, 7217, 12110, 9053, 12970, 2420, 10536, 10835, 13445, 15652, 7907]
result="Y"
for num in range(len(data)-1):
    for n1 in range(128):
        for n2 in range(128):
            for n3 in range(128):
                if n1^n2*n2^n3==data[num]:
                    result+=chr(n2)

print(result)
            
