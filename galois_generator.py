def primitive_checker(p):
    group = set(range(1, p))
    generators = []
    for g in group:
        test_set = set()
        for n in range(1, p):
            a = g**n % p
            test_set.add(a)
        if group.difference(test_set) == set():
            generators.append(g)
    return generators


if __name__ == '__main__':
    p = 47
    generators_list = primitive_checker(p)
    print(generators_list)
    for _ in generators_list:
        print(sorted([_**x % p for x in range(1, p)]))

