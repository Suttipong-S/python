age = int(input ("ป้อนอายุของคุณ : "))

# if not age >= 15 :
#     print("วัยรุ่น")
# else :
#     print("วัยเด็ก")
# Ternary operator
#"เงื่อนไขเป็นจริง" if expression else "เงื่อนไขอื่นๆ"
print("วัยรุ่น") if age >= 15 else print("วัยเด็ก")
print("จบโปรแกรม")