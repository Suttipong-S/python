# โปรแกรมคำนวณค่า BMI (ค่าดัชนีมวลกาย)
#BMI = น้ำหนัก (Kg) / ส่วนสูง * ส่วนสูง (M)

#input and convert to integer

#proccess
#cm => m
# high = high/100
# high /=100 #Compound Assignment ย้ายไปหารตอน input ก็ได้
#cal BMI
#BMI = weight/(high*high)

#output
weight = int(input ("กรุณาป้อนน้ำหนักของคุณ (kg) : "))
high = int(input("ป้อนส่วนสูงของคุณ (cm) : ")) /100

bmi = weight/(high**2)  # Compound Assignment

if bmi >=0 and bmi <= 18.0 : #ป้องกันคนใส่ค่าติดลบ
    result ="ต่ำกว่าเกณฑ์"
elif bmi >= 18.5 and bmi <= 22.9 :
    result ="สมส่วน"
elif bmi >= 23.0 and bmi <= 24.9 :
    result ="น้ำหนักเกิน"
elif bmi >= 25.0 and bmi <= 29.9 :
    result ="โรคอ้วน ระดับที่ 1"
elif bmi >30 :
    result ="โรคอ้วนที่เป็นอันตราย"
else :
    result = "ไม่ทราบค่าที่ชัดเจน"

print("ค่า BMI", bmi,"ทำนายว่า =",result)

'''
< 18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1
> 30 = โรคอ้วนที่เป็นอันตราย
'''
