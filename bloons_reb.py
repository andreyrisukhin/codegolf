
"""
(1) Solve
(2) Minimize soln
"""

"""
Test Cases
Input: 1 red
Output: 1

Input: 7 green
Output: 21

Input: 5 bfb, 11 moab
Output: 22596

Input: 1 red, 2 yellow, 3 white, 4 zebra, 5 moab, 6 ddt
Output: 8110

Input: 1 moab, 1 bfb, 1 zomg, 1 ddt, 1 bad, 1 red, 1 blue, 1 green, 1 yellow, 1 pink, 1 black, 1 white, 1 purple, 1 lead, 1 zebra, 1 rainbow, 1 ceramic
Output: 77257
"""
tests = {
    '1 red': 1,
    '7 green': 21,
    '5 bfb, 11 moab': 22596,
    '1 red, 2 yellow, 3 white, 4 zebra, 5 moab, 6 ddt': 8110,
    '1 moab, 1 bfb, 1 zomg, 1 ddt, 1 bad, 1 red, 1 blue, 1 green, 1 yellow, 1 pink, 1 black, 1 white, 1 purple, 1 lead, 1 zebra, 1 rainbow, 1 ceramic': 77257,
}


map = {
    'red': 1,
    'blue': 2,
    'green': 3,
    'yellow': 4,
    'pink': 5,
    'black': 11,
    'white': 11,
    'purple': 11,
    'lead': 23,
    'zebra': 23,
    'rainbow': 47,
    'ceramic': 104,
    'moab': 616,
    'bfb': 3164,
    'zomg': 16656,
    'ddt': 816,
    'bad': 55760,
}

'''
s is a csv of bloon-count pairs. (Test cases)
'''
def calculate_bloons_rbe(s:str) -> int:
    rbe = 0
    pairs = s.split(', ')
    for p in pairs:
        count, bid = p.split(' ')
        rbe += map[bid] * int(count)
    return rbe

for test, result in tests.items():
    print(f'{test} -> {calculate_bloons_rbe(test)}, expected {result}')