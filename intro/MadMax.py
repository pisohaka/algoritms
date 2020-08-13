def MadMax(N: int, Tele):
    impulse = sorted(Tele)
    middle = int((N - 1)/2)
    impulse.insert(middle, impulse.pop(N-1))
    result = [0 for _ in range(N)]
    result[:middle+1] = sorted(impulse[:middle+1])
    result[middle+1:] = sorted(impulse[middle+1:], reverse=True)
    return result
