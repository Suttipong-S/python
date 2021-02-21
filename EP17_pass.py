#pass เป็นการบอกว่าให้ข้าม process นี้ไปก่อน เพื่อให้ code ยังทำงานไ้อยู่
age = int(input("ป้อนอายุของคุณ :"))

if age <= 15:
    if age == 15:
        pass
        #print("ม.3")
    elif age == 14:
        pass
        #print("ม.2")
    elif age == 13:
        pass
        #print("ม.1")
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")