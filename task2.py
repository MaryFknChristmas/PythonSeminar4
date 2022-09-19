n = int(input("Введите число: "))

def fact(n):
    spisok = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            spisok.append(d)
            n//=d
        else:
            d += 1
    spisok.append(n)
    print(spisok)

fact(n)