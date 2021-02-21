# Loop ซ้อน Loop

# i = 1

# while i<= 3 :
#     #print("รอบที่ :",i)
#     j =1 # ตัวนับ
#     while j <=5:
#         print("รอบที่ i :",i,"ตำแหน่งที่ j = ",j)
#         j = j +1 
#     i = i+1
# print("End Programs")

for i in range(1,4):
    print("รอบที่ i =",i)
    for j in range(1,6): #ให้ปริ้นรอบที่ 1 - 5
        print("ตำแหน่งที่ j =",j)