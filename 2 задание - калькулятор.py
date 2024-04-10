a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
make = str(input("Какая операция? (+, -, *, /): "))
if make == "+":
    c = a + b
    print("Результат:", int(c))
elif make == "-":
    c = a - b
    print("Результат:", int(c))
elif make == "*":
    c = a * b
    print("Результат:", int(c))
elif make == "/":
    if a == 0 or b == 0:
        print("Результат:", int(c))
    else:
        c = a / b
        print("Результат:", int(c))
