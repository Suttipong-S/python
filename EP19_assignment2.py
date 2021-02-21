#แลกเงินและหาจำนวนแบงก์

# 2000 => 1000 => 2 ใบ
# 1500 => 1 ใบ , 500 1 ใบ
# 1800 => 1 ใบ , 500 = 1 ใบ, 100 => 3 ใบ
# 100 => 50 => 2 ใบ


number = int(input("Please Enter you exchange money : "))

if number >= 1000 :
    print("Money 1000 Exchange = ", number//1000, "ใบ") # 1 ใบ
    #number = number % 1000 # 1500%1000 = 500
    number %= 1000

if number >= 500 :
    print("Money 500 Exchange = ", number//500, "ใบ")
    #number = number % 500 เขียนแบบเต็ม
    number%= 500 # เขียนแบบย่อ

if number >= 100 :
    print("Money 100 Exchange = ", number//100, "ใบ")
    #number = number % 100
    number%= 100

if number >= 50 :
    print("Money 50 Exchange = ",number//50,"ใบ")
    #number = number % 50
    number%= 50

if number >= 20 :
    print("Money 20 Exchabge = ",number//20,"ใบ")
    #number = number % 20
    number%= 20


#2000 / 1000 = 2 ใบ
