#ตัวเลขขั้นบันได

'''
input =5
1
12
123
1234
12345
'''
last = int(input("Please enter number :"))

for row in range (1,last+1,1): # 1 ตัวสุดท้ายคือ step หมายถึงเพิ่มทีละ 1 
    for column in range(1,row+1,1):
        print(column,end='')
    print(" ")

'''
input =3

row =1,3
column 1,2
print 1

row =2,3
column 1,3
print 1 2

row =3,3
column 1,4
print 1 2 3
'''