import sys


class QuadraticSolver:

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_coef(index, prompt, args=None):
        if args and len(args) > index:
            value_str = args[index]
            if QuadraticSolver.is_float(value_str):
                return float(value_str)

        while True:
            print(prompt)
            value_str = input().strip()
            if QuadraticSolver.is_float(value_str):
                return float(value_str)
            print("Некорректное значение. Введите действительное число.")

    @staticmethod
    def solve_biquadratic(a, b, c):
        if a == 0:
            raise ValueError("Коэффициент 'a' не может быть равен 0")

        roots = []
        D = b ** 2 - 4 * a * c

        if D < 0:
            return roots

        if D == 0:
            k = -b / (2 * a)
            if k > 0:
                roots.extend([k ** 0.5, -(k ** 0.5)])
            elif k == 0:
                roots.append(0.0)
        else:
            k1 = (-b + D ** 0.5) / (2 * a)
            k2 = (-b - D ** 0.5) / (2 * a)

            if k1 > 0:
                roots.extend([k1 ** 0.5, -(k1 ** 0.5)])
            elif k1 == 0:
                roots.append(0.0)

            if k2 > 0:
                roots.extend([k2 ** 0.5, -(k2 ** 0.5)])
            elif k2 == 0:
                roots.append(0.0)

        # Убираем дубликаты (0.0 может появиться дважды)
        unique_roots = []
        for root in roots:
            if root not in unique_roots:
                unique_roots.append(root)

        return unique_roots

    @staticmethod
    def format_roots(roots):
        rounded_roots = [round(root, 2) for root in roots]

        if len(rounded_roots) == 0:
            return "Действительных корней нет"
        elif len(rounded_roots) == 1:
            return f"Один корень: {rounded_roots[0]}"
        elif len(rounded_roots) == 2:
            return f"Два корня: {rounded_roots[0]} и {rounded_roots[1]}"
        elif len(rounded_roots) == 3:
            return f"Три корня: {rounded_roots[0]}, {rounded_roots[1]} и {rounded_roots[2]}"
        elif len(rounded_roots) == 4:
            return f"Четыре корня: {rounded_roots[0]}, {rounded_roots[1]}, {rounded_roots[2]} и {rounded_roots[3]}"


def main():
    solver = QuadraticSolver()

    # Получаем коэффициенты из аргументов командной строки или через ввод
    a = solver.get_coef(1, "Введите коэффициент A:", sys.argv)
    b = solver.get_coef(2, "Введите коэффициент B:", sys.argv)
    c = solver.get_coef(3, "Введите коэффициент C:", sys.argv)

    try:
        roots = solver.solve_biquadratic(a, b, c)
        result = solver.format_roots(roots)
        print(result)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()