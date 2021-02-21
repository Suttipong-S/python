# สร้างภาพวาด 4 เหลี่ยมจตุรัส

"""
3x3
xxx
xxx
xxx

2x2
xx
xx

5x5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx
"""

number =int(input("ป้อนขนาด ="))

for row in range(0,number,1) :
    for column in range(0,number,1):
        print("x",end="")
    print(" ")
        #print(row,"column",column)

    #print("x",end="")

