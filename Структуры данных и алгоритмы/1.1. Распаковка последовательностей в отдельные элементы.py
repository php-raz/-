p = (4, 5)
x, y = p
print(f'p = {p}\nx = {x}, y = {y}')

print('----------------------')

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(f'data = {data}\nname = {name}, shares = {shares}, price = {price}, date = {date}')

print('----------------------')

s = 'Hello'
a, b, c, d, e = s
print(f's = {s}\na = {a}, b = {b}, c = {c}, d = {d}, e = {e}')

print('----------------------')

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, _, price, _ = data
print(f'data = {data}\nname = {name}, price = {price}')

print('----------------------')
