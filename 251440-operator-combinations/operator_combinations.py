from itertools import product

a, b, c = map(int, input().split("?"))

max_comb = 0
for ops in product("*+", repeat=2):
    expr = eval(f"({a} {ops[0]} {b}) {ops[1]} {c} ")
    max_comb = max(max_comb, expr)
    expr = eval(f"{a} {ops[0]} ({b} {ops[1]} {c})")
    max_comb = max(max_comb, expr)

print(max_comb)
