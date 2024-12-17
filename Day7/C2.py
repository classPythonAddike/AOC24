import os
from concurrent.futures import ProcessPoolExecutor

with open("input.txt") as f:
    eqns = f.readlines()

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def con(a, b):
    return int(str(a) + str(b))

class Operator():
    def __init__(self, value: int, previous: 'Operator' = None, op: int = 0):
        self.value = value
        self.previous = previous
        self.op = op

    def eval(self):
        if self.previous is None:
            return self.value

        return [add, mul, con][self.op](self.previous.eval(), self.value)


    def __str__(self):
        if self.previous is None:
            return str(self.value)

        return f"{str(self.previous)} {('+', '*', '||')[self.op]} {self.value}"

reduced_eqns = []

for eqn in eqns:
    eqn = eqn.strip().split(":")
    lhs = int(eqn[0])
    rhs = list(map(int, eqn[1].split()))

    node = Operator(rhs[0])
    for val in rhs[1:]:
        node = Operator(val, node)

    print(lhs, "\t:", node)
    
    reduced_eqns.append((lhs, node))


def map_operators(ops: str, t_node: Operator):
    cur_node = t_node
    i = 0
    while cur_node.previous is not None:
        cur_node.op = int(ops[i])
        cur_node = cur_node.previous
        i += 1

print("-" * 50)

def ternary(n):
    e = n // 3
    q = n % 3
    return '0' if n == 0 else str(q) if e == 0 else ternary(e) +  str(q)


def return_eval(eqn):
    t = eqn[1]
    l = -1
    while t is not None:
        t = t.previous
        l += 1

    for i in range(3 ** l):
        t = ternary(i)
        map_operators("0" * (l - len(t)) + t, eqn[1])
        
        if eqn[1].eval() == eqn[0]:
            return eqn[0]
    
    return 0

num_eqns = len(eqns)
tot_sum = 0

with ProcessPoolExecutor() as executor:
    for idx, val in enumerate(executor.map(return_eval, reduced_eqns)):
        print(f"\r{idx}/{num_eqns}\t{idx / num_eqns * 100: .2f}%", end="")
        tot_sum += val

print()
print(tot_sum)
