# name = "  beer Love Thailand : 29 มา 29 ต่อ 29  " #index ช่องของตัวอักษารที่อยู่ในข้อความ จะเริ่มต้นที่ 0

# # การเข้าถึงตัวอักษรใน string
# # print(name[0]) # ดึงตัวแรก index ที่ 0 คือ B
# # print(name[1]) # ดึงตัวแรก index ที่ 1 คือ e
# # print(name[2]) # ดึงตัวแรก index ที่ 2 คือ e
# # print(name[0:5]) # ดึงก่อนถึงจุดสุดท้าย
# # print(name[:5]) # ดึงก่อนถึงจุดสุดท้าย ไม่ต้องใส่ตัวแรกก็ได้
# # print(name[0:7]) # ช่องว่างนับเป็น index ด้วย

# # print("อายุเท่าไหร่ = ",name[-2:]) # ก่อนถึงจุดสุดท้าย
# # #การใช้ len function
# # print("ความยาว : ",len(name))

# # print(name)

# # # name = name.strip() #การใช้ strip ลบช่องว่างซ้าย-ขวา
# # # print(len(name))
# # name = name.lstrip() #การใช้ strip ลบช่องว่างซ้าย
# # print(len(name))

# # name = name.rstrip() #การใช้ strip ลบช่องว่างขวา
# # print(len(name))

# # print(name.upper()) # ตัวพิมพ์ใหญ่
# # print(name.lower()) # ตัวพิมพ์เล็ก

# # print(name.capitalize()) # ตัวพิมพ์ใหญ่ตัวแรกสุด

# print(name.replace("beer","Boo")) #แทนที่ข้อความ
# print(name.replace("29","30")) #แทนที่ข้อความ

# print(name.replace("29","30",3)) เปลี่ยนที่เจอ 29 ทั้ง 3 จุด อาจใช้ 2 หรือ 1 ก้ได้

# ''' การเช็คจ้อความ => true , false '''
# name = "ไปซื้อข้าวและอาหารที่ตลาดสด"
# x = "ข้าว" not in name #true , false
# if x :
#     name=name.replace("ข้าว","ไข่")
# print(name)

#7. ารต่อ string (concatinate) +
# fname = "Beer"
# lname = "Susu"
# age = "28"

# print("ชื้อต้น : "+fname+"\tนามสกุล :"+lname+"\tอายุ :"+age)

# #8. การจัดรูปแบบการแสดงผล

# fname = "Beer sasa"
# lname = "Susu code"
# age = "28"
# occup = "audit"
# salary = 500000.509988
# text = "ชื้อต้น :{0} \tนามสกุล :{1} \tอายุ :{2}\tอาชีพ:{3} \tเงินเดือน: {4:.2f}" # การจัด format text #.2f ทศนิยม 2 ตำแหน่ง
# #text = "ชื้อต้น :{} \tนามสกุล :{} \tอายุ :{}" # การจัด format text

#print(text.format(fname,lname,age,occup,salary))

#9. การนับจำนวนคำในประโยค
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด จะเวะไปสวนทุเรียนด้วย"
print(fruit.count("ทุเรียน"))

#10. เช็คคำขึ้นต้น/ คำลงท้าย
name = "นายกอไก่ ใจดี" # เช็คคำขึ้นต้น
if name.startswith("นาย"):
    print("ชาย")
else :
    print("เพศอื่น")
#print(name.startswith("นาย"))

name = "1150" # เช็คคำลงท้าย
if name.endswith("0"):
    print("ถูกหวย")
else :
    print("ไม่ถูกหวย")
#print(name.startswith("นาย"))