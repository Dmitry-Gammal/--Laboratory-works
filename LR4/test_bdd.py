from behave import given, when, then
from main import QuadraticSolver

@given('биквадратное уравнение с коэффициентами {a:g}, {b:g}, {c:g}')
def step_given_equation(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c

@when('я решаю уравнение')
def step_when_solve(context):
    solver = QuadraticSolver()
    context.roots = solver.solve_biquadratic(context.a, context.b, context.c)

@then('должно быть {count:d} действительных корней')
def step_then_roots_count(context, count):
    assert len(context.roots) == count, f"Ожидалось {count} корней, получено {len(context.roots)}"

@given('биквадратное уравнение x^4 - 5x^2 + 4 = 0')
def step_given_specific_equation1(context):
    context.a = 1
    context.b = -5
    context.c = 4

@when('я нахожу его корни')
def step_when_find_roots(context):
    solver = QuadraticSolver()
    context.roots = solver.solve_biquadratic(context.a, context.b, context.c)

@then('корни должны быть ±2 и ±1')
def step_then_specific_roots(context):
    expected_roots = {2.0, -2.0, 1.0, -1.0}
    actual_roots = set(context.roots)
    assert expected_roots == actual_roots, f"Ожидалось {expected_roots}, получено {actual_roots}"

@given('уравнение с {count:d} корнями')
def step_given_equation_with_roots(context, count):
    if count == 0:
        context.a, context.b, context.c = 1, 2, 5
    elif count == 1:
        context.a, context.b, context.c = 1, 0, 0
    elif count == 2:
        context.a, context.b, context.c = 1, 0, -4
    elif count == 4:
        context.a, context.b, context.c = 1, -5, 4

@when('я форматирую результат')
def step_when_format_result(context):
    solver = QuadraticSolver()
    roots = solver.solve_biquadratic(context.a, context.b, context.c)
    context.formatted_result = solver.format_roots(roots)

@then('результат должен содержать "{expected_text}"')
def step_then_contains_text(context, expected_text):
    assert expected_text in context.formatted_result, \
        f"Текст '{expected_text}' не найден в '{context.formatted_result}'"