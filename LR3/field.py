def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        field_name = args[0]
        for item in items:
            value = item.get(field_name)
            if value is not None:
                yield value
    else:
        for item in items:
            result = {}
            has_valid_fields = False
            for arg in args:
                value = item.get(arg)
                result[arg] = value
                has_valid_fields = True
            if has_valid_fields:
                yield result

# Пример:
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
ans = ''
for i in field(goods, 'title'):
    ans += f"'{i}', "
ans = ans[:-2]
print(ans)
# должен выдавать 'Ковер', 'Диван для отдыха'
ans = ''
for i in field(goods, 'title', 'price'):
    ans += f"{i}, "
ans = ans[:-2]
print(ans)
# должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}