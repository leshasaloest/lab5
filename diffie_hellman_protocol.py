from galois_generator import primitive_checker


def prime_checker(p):
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return True
        for i in range(2, p):
            if p % i == 0:
                return False
            return True


def primitive_check(g, p):
    primitive_list = primitive_checker(p)
    if g in primitive_list:
        return True
    else:
        return False


if __name__ == '__main__':
    l = []
    while True:
        P = int(input("Enter P : "))
        if not prime_checker(P):
            print("Number Is Not Prime, Please Enter Again!")
            continue
        break
    while True:
        G = int(input(f"Enter The Primitive Root Of {P} : "))
        if not primitive_check(G, P):
            print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
            continue
        break
    x1, x2 = int(input("Enter The Private Key Of User 1 : ")), int(
        input("Enter The Private Key Of User 2 : "))
    while True:
        if x1 >= P or x2 >= P:
            print(f"Private Key Of Both The Users Should Be Less Than {P}!")
            continue
        break
    y1, y2 = pow(G, x1) % P, pow(G, x2) % P
    k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P
    print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")
    if k1 == k2:
        print("Keys Have Been Exchanged Successfully")
    else:
        print("Keys Have Not Been Exchanged Successfully")
