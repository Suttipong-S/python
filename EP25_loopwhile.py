#โครงสร้างควบคุมแบบทำซ้ำ

# i = 1 # ตัวนับจำนวนรอบ

# while i <=3: # 1<3 ปรั้นรอบ 1 , 2<=3 ปรั้นรอบ 2, 3<=3 ปรั้นรอบ 3, 4<=3 จบการทำงาน
#     print("รอบที่รัน",i)
#     i = i+1 # i เพิ่มค่า 1=2,i เพิ่มค่า 1=3,i เพิ่มค่า 1=4
# print("จบโปรแกรม")

# '''
# while expression :
#     statement
# '''
# #โจทย์ 1+2+3+4+5

# i =1
# summation = 0 # เก็บผลบวกเลขตามจำนวนรอบ
# average = 0 #ผลรวม / จำนวนรอบ
# count = int(input("ระบุจำนวนรอบ :"))
# while i<=count: # while จะทำงานก็ต่อเมื่อเงื่อนไขเป็นจริง
#     summation= summation+i
#     print("ค่า Sum รอบ",i,"ได้",summation)
#     #summation+=i # เก็บผลรวมของ i แต่ละรอบ 1+2+3
#     i=i+1 #1,2,3,4,5
#     #i+=1
# average = summation/10
# print("ผลรวมการบวกเลข : ",summation)
# print("ค่าเฉลี่ย",average)

# summation = 0
# #for i in range(1,6,2): # กำหนดรอบ #ค่าเริ่มต้นที่ 0,1,2  # ปริ้นตั้งแต่ 1-6 และเพิ่มค่าขึ้นทีละ 2
# for i in range(1,11): #summation range(start,stop-1,step)
#     summation = summation +i
#      #print("รอบที่ :",i+1,"Hello World")
#     print("รอบที่ :",i,"sum = ",summation)

# print("ผลรวม : ",summation)     
# print("ค่าเฉลี่ย : ",summation/10)

summation = 0
#for i in range(1,6,2): # กำหนดรอบ #ค่าเริ่มต้นที่ 0,1,2  # ปริ้นตั้งแต่ 1-6 และเพิ่มค่าขึ้นทีละ 2
for i in range(10,0,-1): #การลดค่าที่ละ 1 โดยระบุติด -1 range(start,stop-1,step)
    print("รอบที่ :",i)