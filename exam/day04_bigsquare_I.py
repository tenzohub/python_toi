import time
import tool
tool.memory_usage() #3 บรรทัดนี้ ใช้เพื่อตรวจสอบเวลา และการใช้หน่วยความจำ

qty = int(input())
arr_data = []
for i in range(qty) :
    arr_row = list(map(int,input().split(' ')))
    arr_data.append(arr_row)

start_time = time.time() #ทดสอบจับเวลา
max_cnt = 0
for i in range(qty):
    ref_x = arr_data[i][0]
    ref_y = arr_data[i][1]
    for j in range(qty):
        if (j != i) :
            find_x = arr_data[j][0]
            find_y = arr_data[j][1]
            cnt = ref_x - find_x
            if (find_y + cnt == ref_y) :
                cur_cnt = abs(cnt)
                if (max_cnt < cur_cnt) :
                    max_cnt = cur_cnt

print (max_cnt)

end_time = time.time() #เวลาสิ้นสุด
elapsed_time = end_time - start_time #คำนวณเวลาที่ใช้
print(round(elapsed_time,5), ' Sec') 

tool.memory_usage() #แสดงหน่วยความจำที่เพิ่มขึ้น