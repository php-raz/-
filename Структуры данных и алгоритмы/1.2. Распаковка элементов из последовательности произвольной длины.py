record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(f'record = {record}\nname = {name}, email = {email}, phones_numbers = {phone_numbers}')

print('-----------------------')

sale_records = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing, current = sale_records
print(f'sale_records = {sale_records}\ntrailing = {trailing}, current = {current}')

print('-----------------------')

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]
for tag, *args in records:
    if tag == 'foo':
        print('foo', *args)
    elif tag == 'bar':
        print('bar', *args)

print('-----------------------')

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty/:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(f'line = {line}\nuname = {uname}, fields = {fields}, homedir = {homedir}, sh = {sh}')

print('-----------------------')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(f'record = {record}\nname = {name}, year = {year}')

print('-----------------------')

items = [10, 8, 7, 1, 9, 5, 10, 3]
head, *tail = items
print(f'items = {items}\nhead = {head}, tail = {tail}')
