#ตัวอย่างเขียนอย่างง่ายสำหรับข้อสอบ Beginner
itype = input()
iw = float(input())
ih = float(input())
ans = 0
if (itype == 'T') :
    ans = 0.5 * iw * ih
elif(itype == 'R') : #ในที่นี้ จะใช้เป็น else เลยก็ได้เพราะโจทย์กำหนดว่า ใรับค่า T หรือ R เท่านั้น
    ans = iw * ih
print(ans)