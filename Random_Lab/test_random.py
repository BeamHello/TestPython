import random

for i in range(10):
    p = int(random.uniform(0, 100))
    sucess_rate = 20
    if p < sucess_rate:
        sucess_rate = 20
        print(f"sucess {p} and rate {sucess_rate}")
    else:
        sucess_rate = sucess_rate + 10
        print(f"failed {p} and rate {sucess_rate}")