# โปรแกรมคำนวณค่า BMI (ค่าดัชนีมวลกาย)
#BMI = น้ำหนัก (Kg) / ส่วนสูง * ส่วนสูง (M)

#input and convert to integer
weight = int(input ("กรุณาป้อนน้ำหนักของคุณ (kg) : "))
high = int(input("ป้อนส่วนสูงของคุณ (cm) : ")) /100

#proccess
#cm => m
# high = high/100
# high /=100 #Compound Assignment ย้ายไปหารตอน input ก็ได้
#cal BMI
#BMI = weight/(high*high)
BMI = weight/(high**2)  # Compound Assignment
#output
print("BMI = ", BMI)
