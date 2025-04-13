qty = int(input())
arr_dat = []
for i in range(qty) :
    arr_dat.append(int(input()))

arr_dat.sort()

last_no = 0
icnt = 1
max_cnt = 0
for x in arr_dat:
    if (last_no == x) :
        icnt+=1
    else :
        last_no = x
        icnt = 1
    if (max_cnt < icnt) :
        max_cnt = icnt
print (max_cnt)