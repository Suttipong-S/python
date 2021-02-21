'''
โครงสร้างควบคุม (control structure)
1. แบบลำดับ ทำจาดบนลงล่าง
2. แบบเลือก
3. แบบทำซ้ำ
'''
'''
if expression :
    statement
'''
# and , or , not

# age = int(input ("ป้อนอายุของคุณ : "))

# if age >= 15 and age <= 20:
#     print("วัยรุ่น")
# elif age >= 21 and age <= 29:
#     print("วัยหนุ่มสาว")
# elif age >= 30 and age <= 39:
#     print("วัยผู้ใหญ่")
# elif age >= 80:
#     print("วัยชรา")
# else :
#     print("วัยเด็ก")
# print("จบโปรแกรม")

# age = int(input ("ป้อนอายุของคุณ : "))

# if age >= 15 or age <= 20:
#     print("วัยรุ่น")
# elif age >= 21 or age <= 29:
#     print("วัยหนุ่มสาว")
# else :
#     print("วัยเด็ก")
# print("จบโปรแกรม")

# age = int(input ("ป้อนอายุของคุณ : "))

# if not age >= 15 :
#     print("วัยรุ่น")
# elif age >= 21 :
#     print("วัยหนุ่มสาว")
# else :
#     print("วัยเด็ก")
# print("จบโปรแกรม")

# 15 -20 >= วัยรุ่น
# 21 - 29 >= วัยหนุ่มสาว
# 30 - 39 >= วัยทำงาน

''' 
if จริง :
    ทำอะไร
else :
    ทำอะไร
'''


age = int(input ("ป้อนอายุของคุณ : "))

# if not age >= 15 :
#     print("วัยรุ่น")
# else :
#     print("วัยเด็ก")
# Ternary operator
#"เงื่อนไขเป็นจริง" if expression else "เงื่อนไขอื่นๆ"
print("วัยรุ่น") if age >= 15 else print("วัยเด็ก")
print("จบโปรแกรม")

# point = int(input ("ระบุคำแนนที่คุณได้ : "))

# if point >= 80 :
#     print("ยินดีด้วยคุณเยี่ยมมาก ได้เกรด A")
# elif point >= 70 :
#     print("ยินดีด้วยคุณดีมาก ได้เกรด B")
# elif point >= 60 :
#     print("พยายามอีกนิดนะ พอใช้แล้ว ได้เกรด C")
# elif point >= 50 :
#     print("ต้องพยายามปรังปรุงตังเองนะ ได้ไม่ค่อยดี คุณ ได้เกรด D")
# else :
#     print ("คุณต้องปรังปรุงเร่งด่วนคุณได้เกรด F")
# print("*****จบการคำนวณเกรด*****")

