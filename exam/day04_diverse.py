import time
import tool

tool.memory_usage()

arr_qty = list(map(int,input().split(' '))) #0 0 -> arr_qty[0], arr_qty[1]
qty_x = arr_qty[1]
qty_y = arr_qty[0]

arr_row = []
for y in range(qty_y) :
    arr_in = list(map(int,input().split(' ')))
    arr_row.append(arr_in)

start_time = time.time() #ทดสอบจับเวลา

max_x = qty_x - 5
max_y = qty_y - 5
icnt = cur_x = cur_y = 0
while (cur_x <= max_x) :
    while(cur_y <= max_y) :

        #Loop Check
        set_tree = {''}
        for chk_x in range(cur_x, cur_x+5) :
            for chk_y in range(cur_y, cur_y +5) :
                set_tree.add(arr_row[chk_y][chk_x])
                # print (set_tree)
        if (len(set_tree) > 5) :
            icnt+=1    
        cur_y += 1 #Shift Y

    cur_x += 1 #Shift X
    cur_y = 0 #Reset Y
print('Cnt',icnt)

end_time = time.time()
elapsed_time = end_time - start_time
print(round(elapsed_time,5), ' Sec')

tool.memory_usage()