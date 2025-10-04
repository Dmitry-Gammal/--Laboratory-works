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
        roots.append(-b/ (2 * a))
    else:
        roots.append((-b + D**0.5) / (2 * a))
        roots.append((-b - D**0.5) / (2 * a))
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
    else:
        print("Два корня: ", round(final_roots[0],2), ' и ', round(final_roots[1],2))

if __name__ == "__main__":
    main()



