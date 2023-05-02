password = input('Введіть пароль: ')
is_numeric = False
is_upper = False
is_lower = False
is_spec = False
score = 0

if len(password) < 8:
    print('Необхідна мінімальна кількість символів: 8')
else:
    score += 1
for char in password:
    if char.islower():
        is_lower = True
if not is_lower:
    print('Рекомендація: Добавити маленьку букву')
else:
    score += 1
for char in password:
    if char.isupper():
        is_upper = True
if not is_upper:
    print('Рекомендація: Добавити велику букву')
else:
    score += 1
for char in password:
    if char in "@#%&()$*?:;№!<>./,":
        is_spec = True
if not is_spec:
     print('Рекомендація: Добавити спецсимвол')
else:
    score += 1
for char in password:
    if char.isdigit():
        is_numeric = True
if not is_numeric:
    print('Рекомендація: Добавити цифру')
else:
    score += 1
print(f'Оцінка загалної складності пароля: {score}')
