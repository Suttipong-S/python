
"""
3x3
xxx
xxx
xxx

x = สีน้ำตาล
o = สีขาว
"""
number =int(input("ป้อนขนาด = "))

for row in range(0,number,1) :
    for column in range(0,number,1):
        if (row + column) %2 ==0 :
            print("x",end="")
        else :
            print("o",end="")
    print(" ")
        #print(row,"column",column)

    #print("x",end="")


"""
3x3
row = 0 + column = 0 step เพิ่มทีละ = 1
row = 0 + column = 1 step เพิ่มทีละ = 1
row = 0 + column = 2 step เพิ่มทีละ = 1
ผลที่ได้
xox

row = 1 + column = 0 step เพิ่มทีละ = 1
row = 1 + column = 1 step เพิ่มทีละ = 1
row = 1 + column = 2 step เพิ่มทีละ = 1
ผลที่ได้
oxo

row = 2 + column = 0 step เพิ่มทีละ = 1
row = 2 + column = 1 step เพิ่มทีละ = 1
row = 2 + column = 2 step เพิ่มทีละ = 1
ผลที่ได้
xox

ผลลัพธ์รวม
xox
oxo
xox
"""