
async def transform(value):
    i = 0
    if int(value) <= 0:
        i = 0
    if int(value) in range(1000, 999999):
        i1 = value / 1000
        i2 = int(i1)
        i = f'{i2} тыс'

    if int(value) in range(1000000, 999999999):
        i1 = value / 1000000
        i2 = int(i1)
        i = f'{i2} млн'

    if int(value) in range(1000000000, 999999999999):
        i1 = value / 1000000000
        i2 = int(i1)
        i = f'{i2} млрд'

    if int(value) in range(1000000000000, 999999999999999):
        i1 = value / 1000000000000
        i2 = int(i1)
        i = f'{i2} трлн'

    if int(value) in range(1000000000000000, 999999999999999999):
        i1 = value / 1000000000000000
        i2 = int(i1)
        i = f'{i2} квдр'

    if int(value) in range(1000000000000000000, 999999999999999999999):
        i1 = value / 1000000000000000000
        i2 = int(i1)
        i = f'{i2} квнт'

    if int(value) in range(1_000_000_000_000_000_000_000, 999_999_999_999_999_999_999_999):
        i1 = value / 1000000000000000000000
        i2 = int(i1)
        i = f'{i2} скст'
    if int(value) in range(1000_000_000_000_000_000_000_000, 999_999_999_999_999_999_999_999_999):
        i1 = value / 1000_000_000_000_000_000_000_000
        i2 = round(i1)
        i = f'{i2} трикс'
    if int(value) >= 1000_000_000_000_000_000_000_000_000:
        i1 = value / 1000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} твинкс'
    if int(value) in range(1000000000000000_000_000_000_000_000, 999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} септ'
    if int(value) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} октл'
    if int(value) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} нонл'
    if int(value) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} декал'
    if int(value) in range(1000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} эндк'
    if int(value) in range(1000000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} доктл'
    if int(value) in range(1000000000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} гугл'
    if int(value) in range(1000000000000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} кинд'
    if int(value) in range(1000000000000000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} трипт'
    if int(value) in range(1000000000000000000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} срист'
    if int(value) in range(1000000000000000000000000000000000000000000000000000000000000,
                           999999999999999999999999999999999999999999999999999999999999999):
        i1 = value / 1000000000000000000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} манит'

    if int(value) >= 1000000000000000000000000000000000000000000000000000000000000000:
        i1 = value / 1000000000000000000000000000000000000000000000000000000000000000
        i2 = round(i1)
        i = f'{i2} гвинт'
    return i