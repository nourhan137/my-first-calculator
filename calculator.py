# اول آلة حاسبة لنورهان
num1 = float(input("ادخلي اول رقم: "))
num2 = float(input("ادخلي تاني رقم: "))

print(f"المجموع: {num1 + num2}")
print(f"الطرح: {num1 - num2}")
print(f"الضرب: {num1 * num2}")
if num2 != 0:
    print(f"القسمة: {num1 / num2}")
else:
    print("مينفعش نقسم على صفر!")
