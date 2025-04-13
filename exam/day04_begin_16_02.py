#กรณีศึกษา การใช้ Loop เพื่อหาค่า min
last_min = 0
for x in range(3) :
    int_inp = int(input())
    if (x == 0) :
        last_min = int_inp    
    if (last_min > int_inp) :
        last_min = int_inp
print (last_min)