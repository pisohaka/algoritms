def squirrel(N: int) -> int:
    factorial = 1
    if N >= 1:
        for i in range (1, N+1):
            factorial = factorial * i
    return str(factorial)[0]
