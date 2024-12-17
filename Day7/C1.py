with open("input.txt") as f:
    eqns = f.readlines()

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

class Operator():
    def __init__(self, value: int, previous: 'Operator' = None, op: int = 0):
        self.value = value
        self.previous = previous
        self.op = op

    def eval(self):
        if self.previous is None:
            return self.value

        return [add, mul][self.op](self.previous.eval(), self.value)

    def __str__(self):
        if self.previous is None:
            return str(self.value)
        return f"{str(self.previous)} {'+*'[self.op]} {self.value}"

reduced_eqns = []
tot_sum = 0

for eqn in eqns:
    eqn = eqn.strip().split(":")
    lhs = int(eqn[0])
    rhs = list(map(int, eqn[1].split()))

    node = Operator(rhs[0])
    for val in rhs[1:]:
        node = Operator(val, node)

    print(lhs, "\t:", node)
    
    reduced_eqns.append((lhs, node))


def map_operators(n: int, t_node: Operator):
    cur_node = t_node
    while cur_node is not None:
        cur_node.op = n & 1
        cur_node = cur_node.previous
        n >>= 1

print("-" * 50)

counter = 0
for eqn in reduced_eqns:
    t = eqn[1]
    l = 0
    while t is not None:
        t = t.previous
        l += 1

    for i in range(0, 2 ** l):
        map_operators(i, eqn[1])
        if eqn[1].eval() == eqn[0]:
            counter += 1
            tot_sum += eqn[0]
            print(f"{counter}.", eqn[1], "=", eqn[0])
            break

print(tot_sum)
