async def transform(value):
    ranges = [
        (1000, 'тыс'),
        (1_000_000, 'млн'),
        (1_000_000_000, 'млрд'),
        (1_000_000_000_000, 'трлн'),
        (1_000_000_000_000_000, 'квдр'),
        (1_000_000_000_000_000_000, 'квнт'),
        (1_000_000_000_000_000_000_000, 'скст'),
        (1_000_000_000_000_000_000_000_000, 'трикс'),
        (1_000_000_000_000_000_000_000_000_000, 'твинкс'),
        (1_000_000_000_000_000_000_000_000_000_000, 'септ'),
        (1_000_000_000_000_000_000_000_000_000_000_000, 'октл'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000, 'нонл'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000, 'декал'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'эндк'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'доктл'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'гугл'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'кинд'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'трипт'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'срист'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'манит'),
        (1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 'гвинт')
    ]

    for threshold, label in reversed(ranges):
        if int(value) >= threshold:
            i1 = int(value) / threshold
            i2 = round(i1)
            return f'{i2} {label}'
    return value