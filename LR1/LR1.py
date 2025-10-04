import sys

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_coef(index, promt):
    while True:
        try:
            value_str = sys.argv[index]
            if is_float(value_str):
                break
            else:
                while not(is_float(value_str)):
                    print("Некорректное значение. Введите действительное число на позиции", index)
                    value_str = input()
                break

        except:
            print(promt)
            value_str = input()
            if is_float(value_str):
                break
            else:
                print("Некорректное значение. Введите действительное число.")
    return float(value_str)

def decision(a,b,c):
    roots = []
    D = b**2 - 4 * a * c
    if D < 0:
        return roots
    elif D == 0:
        k = -b/ (2 * a)
        if k > 0:
            roots.append(k**0.5, -(k**0.5))
        if k == 0:
            roots.append(0)
    else:
        k1 = (-b + D**0.5) / (2 * a)
        k2 = (-b - D**0.5) / (2 * a)
        if k1 > 0:
            roots.append(k1**0.5)
            roots.append(-(k1**0.5))
        if k1 == 0:
            roots.append(0)
        if k2 > 0:
            roots.append(k2**0.5)
            roots.append(-(k2**0.5))
        if k2 == 0:
            roots.append(0)
    return roots

def main():
    a = get_coef(1, "Введите коэффициент A:")
    b = get_coef(2, "Введите коэффициент B:")
    c = get_coef(3, "Введите коэффициент C:")
    final_roots = decision(a, b, c)
    if len(final_roots) == 0:
        print("Действительных корней нет")
    elif len(final_roots) == 1:
        print("Один корень: ", round(final_roots[0],2))
    elif len(final_roots) == 2:
        print("Два корня: ", round(final_roots[0],2), ' и ', round(final_roots[1],2))
    elif len(final_roots) == 3:
        print("Три корня: ", round(final_roots[0],2), ' , ', round(final_roots[1],2), " и ", round(final_roots[2],2))
    elif len(final_roots) == 4:
        print("Четыре корня: ", round(final_roots[0],2), ' , ', round(final_roots[1],2), " , ", round(final_roots[2],2), ' и ', round(final_roots[3],2))

if __name__ == "__main__":
    main()



