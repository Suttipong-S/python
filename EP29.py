
start,stop = 1,3
sum = 0
average = 0
while(start<=stop):
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum = sum+number # บวกเลขที่ป้อนแต่ละรอบ
    start= start+1
avg = sum/stop
print("ผลรวม :",sum)
print("ค่าเฉลี่ย :",avg)