#วิธีที่ 2 ตัวอย่างเพื่อการศึกษา การเขียนตรวจสอบผ่าน Loop
arr_chk = ['a','e','i','o','u']
str_in = input()
is_found = False
for x in arr_chk:
    if (x == str_in) :
        is_found = True
if (is_found == True) :
    print ('yes')
else :
    print('no')