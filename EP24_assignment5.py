#แปลงอุณภูมิ
temp = input("ป้อนอุณภูมิ (องศา) : ") #45C

degree = int(temp[:-1]) #45
unit = temp[-1].upper() #C ถ้าใสมาตัวเล็ก ก็แปลงเป็นตัวใหญ่


if unit == "C":
    result = (9 * degree/5) + 32
    unit_result = "ฟาเรนไฮน์"
if unit == "F":
    result = (degree-32)*5/9
    unit_result = "เซลเซียส"

print("แปลงตัวเลข = ",temp, " เป็น ",unit_result, " =" ,result)


'''
if "C":
    #แปลงเป็นฟาเรนไฮน์
if "F":
    #แปลงเป็นเซลเซียส
'''