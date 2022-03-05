from collections import namedtuple

Position = namedtuple('Position', 'x y')
Token = namedtuple('Token', ['key', 'value', 'position'])

t = Token('ABC', 'DEF', Position(1, 2))
assert t.position.x == 1
