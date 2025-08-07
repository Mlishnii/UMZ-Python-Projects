def solve_puzzles(puzzles):
    l = [] # به صورت لیست باید ریترن بشن True/False چون صورت سوال ذکر کرده مقادیر 
    for i in puzzles :
        if i :
            l.append("True") 
        else :
            l.append("False")
    return l




puzzles = [
    "ali", #  بود و کوتیشن نداشت، ولی چون متغیر نبود ارور میگرفتم موقع ران کردن ali این آیتم در اصل 
    1233,
    0,
    "",
    [],
    {},
    'False',
    '0',
    'None',
    None,
    -1,
    [1, 2, 3],
    {'key': 'value'},
    True,
    ' ',
    '[]',
    '[1, 2, 3]',
    '{}',
    "{'a': 1}",
    'True',
    'ali',
    '1234',
    1,
    0.1,
    -0.1,
    True,
    ' ',
    '[]',
    '[1, 2, 3]',
    '{}',
    "{'a': 1}",
    'True',
    'ali',
    '1234',
    1,
    0.1,
    -0.1,
    True,
    ' ',
    '[]',
    '[1, 2, 3]',
    '{}',
    "{'a': 1}",
    'True',
    'ali',
    '1234',
    1,
    0.1,
    -0.1
    ]


a = solve_puzzles(puzzles) 
print(a)