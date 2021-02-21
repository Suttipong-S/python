# break / continue

# i = 1
# while i <= 10:
#     print("รอบที่ i :",i)
#     if (i ==5) :
#         break # เป็นการเช็คค่าตัวแปร i ถ้ามีค่าเท่ากับ 5 ให้จบการทำงานเลย แล้วออกจาก loop ไปทำ else หรือprint เลย
#     i = i +1
# else:
#     print("End Program")
# #print("End Program")

# i = 1
# while i <= 10:
#     print("รอบที่ i :",i)
#     if (i ==5) :
#         break # เป็นการเช็คค่าตัวแปร i ถ้ามีค่าเท่ากับ 5 ให้จบการทำงานเลย แล้วออกจาก loop ไปทำ else หรือprint เลย
#     i = i +1
# print("End Program")

# i = 0
# while i <= 10:
#     i = i +1
#     if (i ==5) :
#         continue # ถ้าค่า i เท่ากับ 5 ให้กระโดดข้ามไม่ต้องปริ้นหรือไม่ต้องทำบรรทัดถัดไป จาก output มันจะไม่ปริ้นบรรทัดที่ 5
#     print("รอบที่ i :",i)
    
# print("End Program")

# i = 0
# while i <= 10:
#     i = i +1
#     if (i %2 !=0) : # i หาร 2 ไม่ลงตัวไม่ต้องแสดงผล ให้กระโดดข้ามไป
#     #if (i %2 ==0) :
#         continue # ถ้าค่า i เท่ากับ 5 ให้กระโดดข้ามไม่ต้องปริ้นหรือไม่ต้องทำบรรทัดถัดไป จาก output มันจะไม่ปริ้นบรรทัดที่ 5
#     print("รอบที่ i :",i)
    
# print("End Program")


# for i in range(1,11):
#     if(i%2 ==0):
#         continue
#     print("รอบที่ : ",i)
# print("End Program")

for i in range(1,11):
    print(i)
    if(i==5): # ถ้า i เท่ากับ 5 ให้หยุดโปรแกรม
        break
print("End Program")